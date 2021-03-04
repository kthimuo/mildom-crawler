import sys
sys.path.append('..')
from mdcrawler.mildom import Mildom

pbid = '10105254-1610795759'
count = 100
mildom = Mildom()
chats = mildom.get_chats_by_pbid(pbid,count=count)
print(len(chats))
print(chats[0])
print('-----')
chats = mildom.get_chats_by_pbid(pbid)
print(len(chats))
print(chats[-1])
