import requests
import json
from model.playback import PlayBack

class Mildom:
    def __init__(self):
        self.__req = requests
        self.user_agent =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'

    def get_playbacks_by_uid(self, uid, count=5):
        url = 'https://cloudac.mildom.com/nonolive/videocontent/profile/playbackList'
        params = {
        'user_id' : uid,
        'limit' : count,
        'page' : '1',
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
            

if __name__ == '__main__':
    uid = '10105254'
    mildom = Mildom()
    playbacks = mildom.get_playbacks_by_uid(uid,count=100)
    print(len(playbacks))
    print(playbacks[-1])
    


        


