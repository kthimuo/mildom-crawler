import requests
import websocket
import json
import _thread
import time

def on_message(ws, message):
    data = json.loads(message)
    timestamp = int(time.time())
    print(timestamp)
    print(data)
    print('========')
room_id = '77777777'
#room_id = '10335833'
url = 'https://cloudac.mildom.com/nonolive/gappserv/live/enterstudio'
params = {
        'user_id':room_id,
        '__platform':'web',
        }
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
        }

res = requests.get(url,params=params,headers=headers).json()['body']
#print(res.json())
room_id = '10001309'
url = 'https://cloudac.mildom.com/nonolive/gappserv/live/enterstudio'
params = {
        'user_id':room_id,
        '__platform':'web',
        }
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
        }

res2 = requests.get(url,params=params,headers=headers).json()['body']
print('live_mode' in res.keys())
print('live_mode' in res2.keys())
#url = 'wss://jp-room1.mildom.com'
#user_agent =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
#
#websocket.enableTrace(True)
#ws = websocket.WebSocketApp(
#            url,
#            on_message = on_message,
#        )
#
#data ={
#        "guestId":"xxx",
#        "roomId":int(room_id),
#        "cmd":"enterRoom",
#        }
#    
#
#def on_open(ws):
#    def run(*args):
#        ws.send(json.dumps(data))
#    _thread.start_new_thread(run, ())
#ws.on_open = on_open
#ws.run_forever()
#
