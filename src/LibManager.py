import requests
import json
from tinydb import TinyDB, Query


class LibManager():
    def __init__(self, credential_helper):
        self.ch = credential_helper
        self.db = TinyDB('media_db.json')


    def get_infos(self):
        info_url = "https://metropol-mediensuche.de/services/de/metropolcard/account/info"

        for cred in self.ch.get_credentials():
            request_headers={'Authorization': f'Bearer {cred["token"]}'}
            r = requests.get(info_url, headers=request_headers)
            return r.json()
