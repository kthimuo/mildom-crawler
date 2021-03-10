import sys
sys.path.append('..')
from mdcrawler.mildom import Mildom

pbid = '10115448-c0b6qgntc1nt495snrp0'
count = 3 
mildom = Mildom()
chats = mildom.get_playback_chats_by_pbid(pbid,count=count)

for chat in chats:
    print(chat)
    print('-----')
