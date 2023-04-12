import requests

class SendMail():
    def __init__(self, api_token) -> None:
        self.url = "https://send.api.mailtrap.io/api/send"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
    
    def send_mail(self):
        payload = "{\"from\":{\"email\":\"mailtrap@thinkjd.de\",\"name\":\"Mailtrap Test\"},\"to\":[{\"email\":\"jd.georgens@gmail.com\"}],\"subject\":\"You are awesome!\",\"text\":\"Congrats for sending test email with Mailtrap!\",\"category\":\"Integration Test\"}"
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        print(response.text)