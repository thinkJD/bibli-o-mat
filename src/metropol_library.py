import requests
import json
from datetime import datetime


class MetropolLibrary():
    # library_id 8726 is the library id for the Metropol Library Mannheim
    def __init__(self, user_id:str, access_token, library_id:int=8726):
        self.library_id = library_id
        self.info_url = "https://metropol-mediensuche.de/services/de/metropolcard/account/info"
        self.renew_url = "https://metropol-mediensuche.de/services/de/metropolcard/prolong"
        self.request_headers={'Authorization': f'Bearer {access_token}'}


    def get_lent_media(self):
        try:
            r = requests.get(self.info_url, headers=self.request_headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        return r.json()['lent']
    
    
    def get_account_info(self):
        try:
            r = requests.get(self.info_url, headers=self.request_headers)
            account_info = {'card_valid': r.json()['validUntil'], 'fees': r.json()['pendingFees']}
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        return account_info


    def get_renewable_media(self):
        lent_media = self.get_lent_media()
        ret_val = list()
        for media in lent_media:
            if media['renewable']:
                ret_val.append(media)
        return ret_val
    
    
    def get_due_media(self, days_before_due:int=3):
        lent_media = self.get_lent_media()
        ret_val = list()
        for media in lent_media:
            due_date = datetime.strptime(media['deadline'], '%Y-%m-%d')
            days_left = due_date - datetime.today()
            if days_left.days < days_before_due:
                ret_val.append(media)
        return ret_val


    def renew_media(self, mediums:list()):
        renewed_media = list()
        for media in mediums:
            request_data = {'libraryId': self.library_id,
                            'recordId': media['prolongData'],
                            'steps':[{"actionId":0}]}
            response = requests.post(self.renew_url, headers=self.request_headers, json=request_data)
            print('got results, try to confirm')
            request_data['steps'].append({"actionId":2})  # actionId 2 "ok"
            response = requests.post(self.renew_url, headers=self.request_headers, json=request_data)
            if response.status_code == 200:
                renewed_media.append(media)
                print(f"Renewed {media['title']}")
        return renewed_media