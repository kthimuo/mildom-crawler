import sys
sys.path.append('..')
from mdcrawler.mildom import Mildom

uid = '10084097'
mildom = Mildom()
user = mildom.get_account_by_uid(uid)
print(user)
