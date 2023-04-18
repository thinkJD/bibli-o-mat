import requests
import time
from tinydb import TinyDB, Query


class CredentialHelper():
    def __init__(self):
        self.db = TinyDB('db.json').table('credentials')

    def get_token(self, card_number: str, password: str, lib_id: int = 8726):
        try:
            r_url = 'https://metropol-mediensuche.de/services/de/metropolcard/auth/login'
            r_body = {"libraryId": lib_id,
                      "userId": card_number, "password": password}
            r = requests.post(r_url, json=r_body)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return r.json()['token']

    def refresh_token(self, card_number: str):
        cred = Query()
        result = self.db.search(cred.id == card_number)
        token = self.get_token(card_number=card_number,
                               password=result[0]['password'])
        self.db.update({'token': token, 'last_refresh': str(
            time.time())}, cred.id == card_number)

    def get_user_id_by_name(self, name: str):
        cred = Query()
        result = self.db.search(cred.name == name)
        if result:
            return result[0]['id']

    def get_credentials(self, user_id: str = None):
        cred = Query()
        if user_id:
            # Return credentials for one id
            result = self.db.search(cred.id == user_id)
            return result[0]
        else:
            # Return all credentials
            return self.db.search(cred.id.exists())

    def add_user(self, name, mail, id, password):
        token = self.get_token(card_number=user_id, password=password)
        self.db.insert({'name': name,
                        'mail': mail,
                        'id': id,
                        'password': password,
                        'token': token,
                        'last_refresh': str(time.time())})
