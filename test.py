import requests
import json
base_url = 'https://www.mildom.com/10658167' 

video_id = '10105254-c0udi0goiibpi5gqn9pg'
time_offset_ms = '4890000'
end_offset_ms = ''
end_offset_ms = '4890000'
timestamp = '2021-03-02T18:07:42.873Z&'
guest_id = 'pc-gp-68daaba9-d178-4e59-9868-e570116d26db'
location= 'Japan|Mie&__country=Japan'
cluster='aws_japan&__platform=web&__la=ja'
pcv='v2.10.25'
sfr='pc'

time_offset_ms = '0'


url = 'https://cloudac.mildom.com/nonolive/videocontent/chat/replay'
params = {
'video_id' : video_id,
'time_offset_ms': time_offset_ms,
'end_offset_ms': end_offset_ms,
'timestamp' : timestamp,
'guest_id' : guest_id,
'accessToken':'',
'location':location,
'cluster':cluster,
'pcv':pcv,
'sfr':sfr
}
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
headers = {
	'user-agent': ua,
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site'
}
res = requests.get(url,headers=headers,params=params).json()
messages = res["body"]["models"][1]["detail"]
messages = res["body"]["models"][0]["detail"]
#print(messages)
#print(len(messages))
#print(messages[0].keys())
#print(messages[0]['time_offset_ms'])
#print(messages[-1]['time_offset_ms'])

#print(messages[0]['end_offset_ms'])
#print(messages[-1]['end_offset_ms'])

for i in range(100):
	res = requests.get(url,headers=headers,params=params).json()
	messages = res["body"]["models"][1]["detail"]
#	print(messages[0]['message_id'])
	print(len(messages))
	next_time=res["body"]["models"][0]["summary"]["end_offset_ms"]				
	params['time_offset_ms'] = next_time 
	print(int(next_time)/1000)
	print('======')
	
	
#print(len(res["body"]["models"]['detail']))
#[1]["detail"]))
