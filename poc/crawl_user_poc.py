import requests
import json

url = 'https://cloudac.mildom.com/nonolive/gappserv/user/profileV2'

user_id = '10105254'
guest_id = 'pc-gp-68daaba9-d178-4e59-9868-e570116d26db'
location= 'Japan|Mie'
country = 'Japan'
cluster='aws_japan&__platform=web&__la=ja'
pcv='v2.10.25'
sfr='pc'

params = {
'user_id' : user_id,
'__platform':'web',
}
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
headers = {
	'user-agent': ua
}
res = requests.get(url,headers=headers,params=params).json()
print(res.keys())

print(res['body'])


