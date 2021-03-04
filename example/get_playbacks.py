import sys
sys.path.append('..')
from mdcrawler.mildom import Mildom

uid = '10084097'
count = 100
mildom = Mildom()
playbacks = mildom.get_playbacks_by_uid(uid,count=count)
print(len(playbacks))
print(playbacks[0])

