import requests
import json


class LibManager():
    def __init__(self, user_id:str, access_token):
        self.info_url = "https://metropol-mediensuche.de/services/de/metropolcard/account/info"
        self.request_headers={'Authorization': f'Bearer {access_token}'}

    def get_lent_media(self):
        try:
            r = requests.get(self.info_url, headers=self.request_headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        return r.json()['lent']

    def renew_media(self, media_id):
        # From day 1: 2€
        # Save cost savings in Database
        pass