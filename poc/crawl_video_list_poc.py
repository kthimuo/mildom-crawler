import requests
import json


url = 'https://cloudac.mildom.com/nonolive/videocontent/profile/playbackList'

user_id = '10105254'
limit = '10000'
page = '1'
timestamp = '2021-03-02T18:07:42.873Z&'
guest_id = 'pc-gp-68daaba9-d178-4e59-9868-e570116d26db'
location= 'Japan|Mie&__country=Japan'
cluster ='aws_japan'
platform ='web'
la = 'ja'
pcv='v2.10.25'
sfr='pc'
params = {
'user_id' : user_id,
'limit' : limit,
'page' : page,
'timestamp' : timestamp,
'guest_id' : guest_id,
}
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
headers = {
	'user-agent': ua
}
res = requests.get(url,headers=headers,params=params).json()
print(len(res['body']))
print(res['body'][-1])
