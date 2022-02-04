import json
from botocore.vendored import requests

TELE_TOKEN='(your-bot-token)'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)


def send_message(text, chat_id):
    final_text =  reverse(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(final_text, chat_id)
    requests.get(url)
    
def reverse(string):
    string = string[::-1]
    return string
    
def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    reply = message['message']['text']
    send_message(reply, chat_id)
    
    return {
        'statusCode': 200
    }
