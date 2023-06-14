import requests
import time
from tinydb import TinyDB, Query


class CredentialHelper():
    def __init__(self, db_path: str):
        self.db = TinyDB(db_path).table('credentials')

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

    def refresh_token(self, user_id: str):
        cred = Query()
        result = self.db.search(cred.id == user_id)
        token = self.get_token(card_number=user_id,
                               password=result[0]['password'])
        self.db.update({'token': token, 'last_refresh': str(
            time.time())}, cred.id == user_id)

    def get_user_id_by_name(self, name: str):
        cred = Query()
        result = self.db.search(cred.name == name)
        if result:
            return result[0]['id']

    def get_user_list(self):
        cred = Query()
        result = self.db.search(cred.id.exists())
        return result

    def get_credentials(self, user_id: str = None):
        cred = Query()
        user = self.db.search(cred.id == user_id)[0]
        # Refresh token if it is older than 14 days or empty
        if ((time.time() - float(user['last_refresh']) > 14 * 24 * 60 * 60) or
                user['token'] == ''):
            print('refreshing access token')
            self.refresh_token(user_id)
            user = self.db.search(cred.id == user_id)[0]
        return user

    def add_user(self, name, mail, id, password):
        token = self.get_token(card_number=id, password=password)
        self.db.insert({'name': name,
                        'mail': mail,
                        'id': id,
                        'password': password,
                        'token': token,
                        'last_refresh': str(time.time())})
