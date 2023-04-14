import mailtrap as mt

class SendMail():
    def __init__(self, api_token) -> None:
        self.client = mt.MailtrapClient(token=api_token)
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        

    def render_mail(self, to:str ):
        mail = mt.Mail(
            sender=mt.Address(email="bibbot@thinkjd.de", name="Mailtrap Test"),
            to=[mt.Address(email=f"{to}")],
            subject="bibli-o-mat hat Geld gespart!",
            text="""
            BeeB Boop ich war fleißig, dass Du es nicht sein musst.
            """,
            )
        return mail
    

    def send_mail(self):
        self.client.send(self.render_mail('jd.goergens@gmail.com'))
        print(response.text)
