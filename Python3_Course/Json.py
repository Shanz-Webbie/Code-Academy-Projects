import json

with open('message.json') as message_json:
  #message_json.open()
  message = json.load(message_json)
print(message['text'])