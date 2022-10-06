import json
import requests
from hyper.contrib import HTTP20Adapter

# add path
CERT = 'cert.pem' 
KEY = 'key.pem'

TOKEN = 'a1b2c....3d4' # add token
TOPIC = 'web.com....' # add website push id

# payload
PAYLOAD = {
  "aps": {
    "alert": {
      "title": title,  # add title
      "body": body,  # add body
      "action-loc-key": button  # add button
    },
    "content-available": 1,
    "url-args": ["arg1", "arg2"]  # add url arguments 
  }
}

def send_safari_notification(token, payload, cert, key, topic):
    session = requests.Session()
    session.mount('https://', HTTP20Adapter())
    session.cert = (cert, key)

    url = 'https://api.push.apple.com/3/device/%s' % token
    headers = {"apns-topic": topic, "apns-push-type": "alert"}
    response = session.post(url=url, data=json.dumps(payload), headers=headers)
    if response.ok:
      print("Push Notification Sent")
    else:
      print("Failed To Send Push Notification")
  
if __name__ == '__main__':
    send_safari_notification(TOKEN, PAYLOAD, CERT, KEY, TOPIC)
