import mailtrap as mt


class SendMail():
    def __init__(self, api_token) -> None:
        self.client = mt.MailtrapClient(token=api_token)
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def render_mail(self, to_address: str, mediums: list, account_info: dict):
        # build table
        table = ""
        for medium in mediums:
            row = f"📅 {medium['deadline']} 📗 {medium['title']}\n  Author: {medium['author']}\n  Format: {medium['format']}\n\n"
            table += row

        cost_saved = len(mediums) * 2

        mail = mt.Mail(
            sender=mt.Address(email="bibli-o-mat@thinkjd.de",
                              name="Bibli-o-mat"),
            to=[mt.Address(email=f"{to_address}")],
            subject=f"bibli-o-mat hat Geld gespart!",
            text=f"""
Beep Boop 🤖

Ich war fleißig, dass Du es nicht sein musst.
Mit Freude habe ich folgende Medien verlängert:

{table}
Du musst nicht zur Bibliothek und musst keine
{cost_saved}€ Säumnisgebühr zahlen 🤑.

Hier noch einige infos zu deinem Konto:
Karte gültig bis: {account_info['card_valid']}
Angefallene Kosten: {account_info['fees']}

bibli-o-mat over and out 🚀

P.S.: Bitte nicht auf die Mail antworten, ich
habe kein Postfach und den Sicherheitscheck
für die Sendedomain nur haarscharf bestanden.
🎤🫳🏻
""",
        )
        return mail

    def send_mail(self, to_address: str, mediums: list, account_info: dict):
        mail = self.render_mail(to_address, mediums, account_info)
        self.client.send(mail)
        print('Mail send to', to_address)
