#!/usr/bin/env python3

import typer
import json
import time
from tinydb import TinyDB, Query
from rich.console import Console
from rich.table import Table
from rich import print
from credential_helper import CredentialHelper
from metropol_library import MetropolLibrary
from send_mail import SendMail


console = Console()
app = typer.Typer()

ch = CredentialHelper()
lm = None
user_id = None
user_mail = None
db = TinyDB('db.json').table('history')


def setup(user_name: str):
    global lm
    global user_id
    global user_mail
    user_id = ch.get_user_id_by_name(user_name)
    credentials = ch.get_credentials(user_id)
    user_mail = credentials['mail']
    lm = MetropolLibrary(credentials['id'], credentials['token'])


@app.command()
def add_user(name:str, mail:str, id: str, password: str):
    ch.add_user(name, mail, id, password)


@app.command()
def list_users():
    table = Table('Name', 'Email', 'ID')
    for user in ch.get_credentials():
        table.add_row(user['name'], user['mail'], user['id'])
    console.print(table)


@app.command()
def list_media(user_name: str = typer.Argument(..., envvar="USER_NAME")):
    setup(user_name)
    lent_media = lm.get_lent_media()

    db.insert({'user_id': user_id, 'lent_media': lent_media, 'timestamp': str(time.time())})

    table = Table("Title", "Author", "Due Date")
    for media in lent_media:
        table.add_row(media['title'], media['author'], media['deadline'])
    console.print(table)


@app.command()
def renewable_media(user_name: str = typer.Argument(..., envvar="USER_NAME")):
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
def get_due_media(user_name: str = typer.Argument(..., envvar="USER_NAME")):
    setup(user_name)
    due_media = lm.get_due_media()
    if not due_media:
        print("No due media found.")
        return
    
    table = Table("Title", "Author", "Due Date")
    for media in due_media:
        table.add_row(media['title'], media['author'], media['deadline'])
    console.print(table)
    

@app.command()
def renew_media():
    setup()
    renewable_media = lm.get_renewable_media()
    if not renewable_media:
        print("No renewable media found.")
        return
    lm.renew_media(renewable_media)
    print("Renewed media, sending mail...")
    sm = SendMail(api_token)


@app.command()
def get_account_info(user_name: str = typer.Argument(..., envvar="USER_NAME")):
    # TODO: Add some functionality arround this
    setup(user_name)
    account_info = lm.get_account_info()
    print(account_info)


@app.command()
def test_mail(
    api_token: str = typer.Argument(..., envvar="MAILTRAP_API_TOKEN"), 
    user_name: str = typer.Argument(..., envvar="USER_NAME")
    ):
    
    setup(user_name)
    mediums = lm.get_renewable_media()
    sm = SendMail(api_token)
    sm.send_mail(user_mail, mediums)


if __name__ == "__main__":
    app()