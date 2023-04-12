#!/usr/bin/env python3

import typer
import json
import time
from tinydb import TinyDB, Query
from rich.console import Console
from rich.table import Table
from rich import print
from CredentialHelper import CredentialHelper
from LibManager import LibManager
from send_mail import SendMail


console = Console()
app = typer.Typer()
ch = CredentialHelper()
user_id = None
lm = None
db = TinyDB('db.json').table('history')


def setup():
    global user_id
    global lm
    user_id = ch.get_credentials()[0]['user_id']
    lm = LibManager(user_id, ch.get_credentials()[0]['token'])

@app.command()
def add_user(user_name:str, user_id: str, password: str):
    ch.add_user(user_name, user_id, password)

@app.command()
def list_users():
    setup()
    table = Table("User Name", "User ID")
    for user in ch.get_credentials():
        table.add_row(user['user_name'], user['user_id'])
    console.print(table)

@app.command()
def list_media():
    setup()
    # TODO: Add option to filter by user
    lent_media = lm.get_lent_media()

    db.insert({'user_id': user_id, 'lent_media': lent_media, 'timestamp': str(time.time())})

    table = Table("Title", "Author", "Due Date")
    for media in lent_media:
        table.add_row(media['title'], media['author'], media['deadline'])
    console.print(table)
    
@app.command()
def renewable_media():
    setup()
    renewable_media = lm.get_renewable_media()
    if not renewable_media:
        print("No renewable media found.")
        return
    
    table = Table("Title", "Author", "Due Date")
    for media in renewable_media:
        table.add_row(media['title'], media['author'], media['deadline'])
    console.print(table)
    
@app.command()
def get_due_media():
    setup()
    due_media = lm.get_due_media()
    if not due_media:
        print("No due media found.")
        return
    
    table = Table("Title", "Author", "Due Date")
    for media in due_media:
        table.add_row(media['title'], media['author'], media['deadline'])
    console.print(table)
    
@app.command()
def send_mail(api_token: str):
    sm = SendMail(api_token)
    sm.send_mail()


if __name__ == "__main__":
    app()