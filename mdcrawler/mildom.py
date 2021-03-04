import requests
import json
from model.playback import PlayBack
from model.user import User
from model.chat import Chat
import endpoints
import time

class Mildom:
    def __init__(self):
        self.__req = requests
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

    def get_chats_by_pbid(self, pbid, count=100):
        '''
        pbid -> PlayBackId
        '''
        length = self.get_playback_lengh_by_pbid(pbid)
        time_offset_ms = 0
        end_offset_ms = ''
        end_offset_ms = ''
        next_time = 0
        chats = []
        cnt = 0

        while cnt <= count and next_time <= length :
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
                    chat = Chat(arr)
                    cnt +=1
                    chats.append(chat)
            next_time = res["body"]["models"][-1]["summary"]["end_offset_ms"]
            time_offset_ms = next_time
            time.sleep(self.sleep_sec)
        return chats    



if __name__ == '__main__':
    import sys
    from model.user import User
    uid = '10084097'
    pbid = '10105254-1610795759'
    mildom = Mildom()

#    user = mildom.get_account_by_uid(uid)
#    playbacks = mildom.get_playbacks_by_uid(uid,count=100)
#    playback = playbacks[0]
#    pbid = playback.pbid
#    chats = mildom.get_chats_by_pbid(pbid,count=1000)
#    print(user)
#    print('-----------')
#    print(playback)
#    print('-----------')
#    print(chats[0])


    


        


