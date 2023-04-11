import requests
import json
from datetime import datetime


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
    
    
    def get_renewable_media(self):
        lent_media = self.get_lent_media()
        ret_val = list()
        for media in lent_media:
            if media['renewable']:
                ret_val.append(media)
        return ret_val
    
    
    def get_due_media(self, days_before_due:int=5):
        lent_media = self.get_lent_media()
        ret_val = list()
        for media in lent_media:
            due_date = datetime.strptime(media['deadline'], '%Y-%m-%d')
            days_left = due_date - datetime.today()
            if days_left.days < days_before_due:
                ret_val.append(media)
        return ret_val


    def renew_media(self, media_id):
        due_media = self.get_due_media()
        cost_saved = len(due_media) * 2
        # TODO: Renew