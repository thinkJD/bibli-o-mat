#!/usr/bin/env python3

import typer
import json
from rich import print_json
from CredentialHelper import CredentialHelper
from LibManager import LibManager


app = typer.Typer()


@app.command()
def add_user(user_id: str, password: str):
    ch = CredentialHelper()
    ch.add_user(user_id, password)


@app.command()
def get_credentials():
    ch = CredentialHelper()
    print_json(json.dumps(ch.get_credentials()))

@app.command()
def get_infos():
    ch = CredentialHelper()
    lm = LibManager(ch)
    print_json(json.dumps(lm.get_infos()))


if __name__ == "__main__":
    app()