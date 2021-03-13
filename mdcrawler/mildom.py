import os
import requests
import websocket
import _thread
import json
import time
from .model.playback import PlayBack
from .model.user import User
from .model.chat import PlayBackChat
from .model.chat import RoomChat
from .model.room import Room
from . import endpoints

class Mildom:
    def __init__(self):
        self.__req = requests
        self.__ws = requests
        self.__ws = websocket
        self.user_agent =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
        self.sleep_sec = 1.0

    def get_playbacks_by_uid(self, uid, count=5):
        params = {
        'user_id' : uid,
        'limit' : count,
        }
        headers = {
            'user-agent': self.user_agent
        }
        res = self.__req.get(
                endpoints.PLAYBACK_LIST_URL,
                headers=headers,
                params=params).json()
        playbacks = []
        for p in res['body']:
            playback = PlayBack(p)
            playbacks.append(playback)
        return playbacks
            
    def get_account_by_uid(self, uid):
        params = {
        'user_id' : uid,
        '__platform':'web',
        }
        headers = {
            'user-agent': self.user_agent
        }
        res = self.__req.get(endpoints.PROFILE_URL,
                headers=headers,
                params=params).json()
        user = User(res['body'])
        return user

    def get_playback_lengh_by_pbid(self,pbid):
        params = {
        'v_id' : pbid,
        '__platform':'web',
        }
        headers = {
            'user-agent': self.user_agent
        }
        res = self.__req.get(endpoints.PLAYBACK_URL,
                headers=headers,
                params=params).json()
        length = int(res['body']['playback']['video_length'])
        return length

    def get_playback_chats_by_pbid(self, pbid, count=None):
        '''
        pbid -> PlayBackId
        '''
        if not count:
            index = float('inf')
        else :
            index = count

        length = self.get_playback_lengh_by_pbid(pbid)
        time_offset_ms = 0
        end_offset_ms = ''
        end_offset_ms = ''
        next_time = 0
        chats = []
        cnt = 0

        while cnt <= index and next_time <= length :
            params = {
            'video_id' : pbid,
            'time_offset_ms': time_offset_ms,
            'end_offset_ms': end_offset_ms,
            }
            headers = {
                'user-agent': self.user_agent,
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site'
            }
            res = requests.get(endpoints.CHAT_URL,headers=headers,params=params).json()
            models = res["body"]["models"]
            for i in range(len(models)):
                detail = res["body"]["models"][i]["detail"]
                for arr in detail:
                    arr['pbid'] = pbid
                    chat = PlayBackChat(arr)
                    cnt +=1
                    chats.append(chat)
            next_time = res["body"]["models"][-1]["summary"]["end_offset_ms"]
            time_offset_ms = next_time
            time.sleep(self.sleep_sec)
        if  count:
            chats = chats[:count]
        return chats    


    def get_room_meta_by_uid(self,uid):
        params = {
                'user_id':uid,
                '__platform':'web',
                }
        headers = {
                'User-Agent':self.user_agent
                }

        arr = requests.get(endpoints.LIVE_META_URL,params=params,headers=headers).json()['body']
        room = Room(arr)
        return room
    
    def observe_room(self,uid,path_to_save='./',view_order=('viewer_count','room_chat'),save_order=('viewer_count','room_chat')):
        room = self.get_room_meta_by_uid(uid)
        start_timestamp = str(room.start_timestamp)
        if path_to_save :
            save_dir = path_to_save + '/' + uid
            os.makedirs(save_dir,exist_ok=True)

            chat_file_name = save_dir +'/'+ start_timestamp + '_chats.txt' 
            viewer_count_file_name = save_dir +'/' + start_timestamp + '_viewer_count.txt' 
            meta_file_name = save_dir +'/' + start_timestamp + '_meta.txt' 
            with open(meta_file_name, 'a') as f:
                c = json.dumps(room.__dict__)
                print(c, file=f)
                print(room)


        data ={
                "guestId":"xxx",
                "roomId":int(uid),
                "cmd":"enterRoom",
                }
        def on_message(ws, message):
            timestamp = int(time.time())
            arr = json.loads(message)
            if arr['cmd'] == 'onChat':
                room_chat = RoomChat(arr)
                if path_to_save:
                    with open(chat_file_name, 'a') as f:
                        c = json.dumps(room_chat.__dict__)
                        print(c, file=f)
                        print(room_chat)

            if (arr['cmd'] == 'onAdd') or (arr['cmd'] == 'userCount'):
                viewer_count = arr['userCount']
                result_dict = {
                        'timestamp':str(int(time.time())),
                        'viewer_count':viewer_count
                        }
                if path_to_save:
                    with open(viewer_count_file_name,'a') as ff:
                        result = json.dumps(result_dict) 
                        print(result, file=ff)
                        print(result)
                        
                


        def on_open(ws):
            def run(*args):
                ws.send(json.dumps(data))
            _thread.start_new_thread(run, ())

        ws = websocket.WebSocketApp(
            endpoints.LIVE_URL ,
            on_message = on_message,
        )
        ws.on_open = on_open
        ws.run_forever()

        
    





        


