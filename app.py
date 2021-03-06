import os
import sys
import json
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from bot.bot_interface import BotInterface

app = Flask(__name__)
bi  = BotInterface()


@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves, and must mention us!
  if data['name'] != 'Infinite' and 'infinite' in data['text'].lower():
    msg = {}
    msg['author']    = data['name']
    msg['author_id'] = data['sender_id']
    msg['text']      = data['text']

    
    reply = bi.process_message(msg)
    if reply:
      send_message(reply['text'])

  return "ok", 200

@app.route('/canned', methods=['POST'])
def canned_webhook():
  data = request.get_json()
  print(data)
  reply = bi.canned_reply(data['topic'])
  send_message(reply['text'])

  return "ok", 200


def send_message(msg):
  if 'BLOOMBOT_DEBUG' in os.environ:
    print('[Infinite]: ' + msg)
    return
    
  # if not in debug mode, use the right url 
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : 'd166405f1751e36deebf1a9b15',
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
