import requests
import json
from model.playback import PlayBack
from model.user import User

class Mildom:
    def __init__(self):
        self.__req = requests
        self.user_agent =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'

    def get_playbacks_by_uid(self, uid, count=5):
        url = 'https://cloudac.mildom.com/nonolive/videocontent/profile/playbackList'
        params = {
        'user_id' : uid,
        'limit' : count,
        }

        headers = {
            'user-agent': self.user_agent
        }
        res = self.__req.get(url,headers=headers,params=params).json()

        playbacks = []
        for p in res['body']:
            playback = PlayBack(p)
            playbacks.append(playback)

        return playbacks
            
    def get_account_by_uid(self, uid):

        url = 'https://cloudac.mildom.com/nonolive/gappserv/user/profileV2'
        params = {
        'user_id' : uid,
        '__platform':'web',
        }
        headers = {
            'user-agent': self.user_agent
        }
        res = self.__req.get(url,headers=headers,params=params).json()
        user = User(res['body'])
        return user


if __name__ == '__main__':
    uid = '10084097'
    mildom = Mildom()
    playbacks = mildom.get_playbacks_by_uid(uid,count=100)
    user = mildom.get_account_by_uid(uid)
    print(len(playbacks))
    print(playbacks[-1])
    print(user)
    


        


