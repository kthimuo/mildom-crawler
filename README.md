## mildom_crawler

This is a Mildom(https://www.mildom.com/) crawler written in Python.

## Install

```
pip install mdcrawler
```

## Example

・Getting user info

```
from mdcrawler.mildom import Mildom

uid = '10084097'
mildom = Mildom()
user = mildom.get_account_by_uid(uid)
print(user)

# then you get
​```
User info:
Username: TIE Ru
UserId: 10084097
Follower: 197449
Follow: 24
Country: Japan
Level: 97
Exp: 332865
GiftRevenue: 2853554
​```
```

・Getting playbacks by user_id

```
from mdcrawler.mildom import Mildom

uid = '10084097'
count = 100
mildom = Mildom()
playbacks = mildom.get_playbacks_by_uid(uid,count=count)
print(len(playbacks))
print(playbacks[0])

# then you get
​```
100

PlayBack info:
PlayBackId: 10084097-c10clv52lrnf4dhgicsg
Username: TIE Ru
UserId: 10084097
PublishTime: 1614859237
Title: 【Apex】渋谷ハルカスタムに渋谷ハルと出る | with prize
ViewNum: 320
Length: 8368110
​```
```

・Getting chats on the playback

```
from mdcrawler.mildom import Mildom

pbid = '10105254-1610795759'
count = 100
mildom = Mildom()

chats = mildom.get_chats_by_pbid(pbid,count=count)
print(len(chats))
print(chats[0])

print('-----')

chats = mildom.get_playbackchats_by_pbid(pbid)
print(len(chats))
print(chats[-1])

# then you get
​```
100

Chat info:
ChatId: 1610795770425_10904046_4711
ChatText: こんだよ～
ChatTime: 1610795770
ChatTimeOffset: 10
Username: fusianasan
UserId: 10904046
PlayBackId: 10105254-1610795759

-----
312

Chat info:
ChatId: 1610796391638_10614220_6151
ChatText: なんだろ
ChatTime: 1610796391
ChatTimeOffset: 631
Username: Leimy
UserId: 10614220
PlayBackId: 10105254-1610795759
​```
```

