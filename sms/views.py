from flask import Blueprint, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from sms.utils import parse_message
import os

sms_svc = Blueprint('SMS', __name__)

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
sms_client = Client(account_sid, auth_token)

FROM = '+12012988195'
MESSAGE_RESPONSE = 'Thank you for reaching Minted Customer Service. Your callback request is scheduled for {0} {1}'

@sms_svc.route('/')
def index():
    return 'Welcome to Minted SMS Service!'

@sms_svc.route('/send', methods=['POST'])
def send():
    content = request.get_json()
    to = content.get('to', None)
    msg = content.get('message', None)
    if sms_client and to and msg:
        sms_client.messages.create(
            to= to,
            from_= FROM,
            body= msg
            )
        return "Successfully sent the message to [{0}]!".format(to)
    return "Error Sending the message!"

@sms_svc.route('/reply', methods=['GET','POST'])
def receive():
    if request.method == 'POST':
        from_no = request.values.get('From')
        message = request.values.get('Body')
        if 'request' in message.lower():
            req_time, req_date = parse_message(message)
            resp = MessagingResponse()
            resp.message(MESSAGE_RESPONSE.format(req_time, req_date))
        return str(resp)
    else:
        return 'No Messages Available!'
