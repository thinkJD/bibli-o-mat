import requests
import time
from tinydb import TinyDB, Query


class CredentialHelper():
    def __init__(self):
        self.db = TinyDB('db.json').table('credentials')
        
    def renew_token(self, card_number:str, password:str, lib_id:int=8726):
        try:
            r_url  = 'https://metropol-mediensuche.de/services/de/metropolcard/auth/login'
            r_body = {"libraryId":lib_id, "userId":card_number,"password":password}
            r = requests.post(r_url, json=r_body)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}') 
        return r.json()

    
    def get_credentials(self):
        cred = Query()
        return self.db.search(cred.user_id.exists())


    def add_user(self, user_name, user_id, password):
        token = self.renew_token(card_number=user_id, password=password)['token']
        self.db.insert({'user_name': user_name, 'user_id': user_id, 'password': password, 'token': token, 'last_refresh': str(time.time())})
