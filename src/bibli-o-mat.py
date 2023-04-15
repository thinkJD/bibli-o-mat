#!/usr/bin/env python3

import typer
import json
import time
import os
from tinydb import TinyDB, Query
from rich.console import Console
from rich.table import Table
from rich import print
from credential_helper import CredentialHelper
from metropol_library import MetropolLibrary
from send_mail import SendMail


console = Console()
app = typer.Typer()

MAILTRAP_API_TOKEN = os.getenv('MAILTRAP_API_TOKEN')

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
def user_token_refresh(card_number:str):
    ch.refresh_token(card_number)
    console.print(f"Refreshed token for {card_number}")


@app.command()
def list_lent(user_name: str = typer.Option(..., prompt=True)):
    setup(user_name)
    lent_media = lm.get_lent_media()

    db.insert({'user_id': user_id, 'lent_media': lent_media, 'timestamp': str(time.time())})

    table = Table("Title", "Author", "Due Date")
    for media in lent_media:
        if media['renewable']:
            deadline = f'{media["deadline"]} 🚀'
        else:
            deadline = media["deadline"]
        table.add_row(media['title'], media['author'], deadline)
    console.print(table)


@app.command()
def list_renewable(user_name: str = typer.Option(..., prompt=True)):
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
def list_due(user_name: str = typer.Option(..., prompt=True)):
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
def renew(user_name: str = typer.Option(..., prompt=True)):
    setup(user_name)
    renewable_media = lm.get_renewable_media()
    if not renewable_media:
        print("No renewable media found.")
        return

    renewed = lm.renew_media(renewable_media, count=1)
    print("Renewed media, sending mail...")
    sm = SendMail(MAILTRAP_API_TOKEN)
    sm.send_mail(user_mail, renewed, lm.get_account_info())
    print ('Done')


@app.command()
def account_info(user_name: str = typer.Option(..., prompt=True)):
    setup(user_name)
    account_info = lm.get_account_info()
    print(account_info)


if __name__ == "__main__":
    app()