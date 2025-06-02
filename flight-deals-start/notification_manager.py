from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    
    def __init__(self):
        self.client = Client(os.environ["ACCOUNT_SID"],os.environ["AUTH_TOKEN"])

    def send_sms(self,message_body):

        message = self.client.messages.create(body=message_body,
         from_= os.environ["TWILIO_VIRTUAL_NUMBER"],
         to= os.environ["TWILIO_VERIFIED_NUMBER"])
        
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)
