import typer
import json
import time
import os
from tinydb import TinyDB, Query
from rich.console import Console
from rich.table import Table
from rich import print
from .credential_helper import CredentialHelper
from .metropol_library import MetropolLibrary
from .send_mail import SendMail
from .brain import SemanticKernel


console = Console()
app = typer.Typer()

MAILTRAP_API_TOKEN = os.getenv('MAILTRAP_API_TOKEN', None)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', None)
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID', None)

if not os.path.exists('data'):
    os.mkdir('data')
db_path = os.path.join('data', 'db.json')

ch = CredentialHelper(db_path)
lm = None
user_id = None
user_mail = None
db = TinyDB(db_path).table('history')


def setup(user_name: str):
    global lm
    global user_id
    global user_mail
    user_id = ch.get_user_id_by_name(user_name)
    credentials = ch.get_credentials(user_id)
    user_mail = credentials['mail']
    lm = MetropolLibrary(credentials['id'], credentials['token'])


@app.command()
def add_user(name: str, mail: str, id: str, password: str):
    """Add a new user to bibli-o-mat.

    Args:
        name (str): Name of the user use unique names.
        mail (str): email address of the user.
        id (str): Library card number.
        password (str): passwort of the user. Defaults to the card owners birthdate.
    """
    ch.add_user(name, mail, id, password)


@app.command()
def list_users():
    """list all bibli-o-mat users.
    """
    table = Table('Name', 'Email', 'ID')
    for user in ch.get_credentials():
        table.add_row(user['name'], user['mail'], user['id'])
    console.print(table)


@app.command()
def list_lent(user_name: str):
    """List all lent media of a user. There is also an indicator if the medium
    is renewable.

       Args:
            user_name (str): Name of the user (the first parameter of add-user)
    """
    setup(user_name)
    lent_media = lm.get_lent_media()

    db.insert({'user_id': user_id, 'lent_media': lent_media,
              'timestamp': str(time.time())})

    table = Table("Title", "Author", "Due Date")
    for media in lent_media:
        if media['renewable']:
            deadline = f'{media["deadline"]} 🚀'
        else:
            deadline = media["deadline"]
        table.add_row(media['title'], media['author'], deadline)
    console.print(table)


@app.command()
def list_renewable(user_name: str):
    """List renewable media of a user. A medium is for example not renewable
    if it is already renewed 3 times.

    Args:
        user_name (str): Name of the user (the first parameter of add-user)
    """
    setup(user_name)
    renewable_media = lm.get_renewable_media()
    if not renewable_media:
        print("No renewable media found.")
        return

    table = Table("Title", "Author", "Due Date")
    for media in renewable_media:
        table.add_row(media['title'], media['author'], media['deadline'])
    console.print(table)


@app.command()
def list_due(user_name: str):
    """List due media of a user. A medium is due if it is three days before
    the deadline.

    Args:
        user_name (str): Name of the user (the first parameter of add-user)
    """
    setup(user_name)
    due_media = lm.get_due_media()
    if not due_media:
        console.print("No due media found.")
        return

    table = Table("Title", "Author", "Due Date")
    for media in due_media:
        table.add_row(media['title'], media['author'], media['deadline'])
    console.print(table)


@app.command()
def renew(user_name: str):
    """Auto renew all due renewable media of a user and send a info mail.

    Args:
        user_name (str): Name of the user (the first parameter of add-user)
    """
    setup(user_name)
    renewable_media = lm.get_renewable_media()
    if not renewable_media:
        console.print("No renewable media found.")
        return

    renewed = lm.renew_media(renewable_media, count=1)
    console.print("media renewed, sending mail...")
    sm = SendMail(MAILTRAP_API_TOKEN)
    sm.send_mail(user_mail, renewed, lm.get_account_info())
    console.print('Done')

@app.command()
def test():
    setup(user_name="Fynn")
    sk = SemanticKernel(OPENAI_API_KEY, OPENAI_ORG_ID)
    book_list = ""
    for medium in lm.get_lent_media():
        book_list += f"{medium['title']} \n"
    console.print(sk.get_short_story(book_list))