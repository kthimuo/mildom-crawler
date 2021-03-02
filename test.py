import requests
import json
base_url = 'https://www.mildom.com/10658167' 

url = base_url + '/live/10658167_540p.m3u8?timestamp=2021-03-02T17:48:35.074Z&__guest_id=pc-gp-68daaba9-d178-4e59-9868-e570116d26db&__location=Japan|Mie&__country=Japan&__cluster=aws_japan&__platform=web&__la=ja&__pcv=v2.10.25&sfr=pc&accessToken=&streamReqId=7278574a-c354-4395-adfb-2c1b22e19ca2&is_lhls=0'

url = 'https://do8w5ym3okkik.cloudfront.net/live/10658167-1614682525633-12793_540p.ts?timestamp=2021-03-02T17:52:11.425Z&__guest_id=pc-gp-68daaba9-d178-4e59-9868-e570116d26db&__location=Japan|Mie&__country=Japan&__cluster=aws_japan&__platform=web&__la=ja&__pcv=v2.10.25&sfr=pc&accessToken=&streamReqId=6d17e4c5-d556-4c06-b5e0-9a8beb14f0c4&is_lhls=0'

url = 'https://d3ooprpqd2179o.cloudfront.net/vod/jp/10105254/10105254-c0v3djd2lrn94g81uapg/origin/720p/10105254-c0v3djd2lrn94g81uapg_720p-1118.ts'

video_id = '10105254-c0udi0goiibpi5gqn9pg'
time_offset_ms = '4890000'
end_offset_ms = ''
timestamp = '2021-03-02T18:07:42.873Z&'
guest_id = 'pc-gp-68daaba9-d178-4e59-9868-e570116d26db'
location= 'Japan|Mie&__country=Japan'
cluster='aws_japan&__platform=web&__la=ja'
pcv='v2.10.25'
sfr='pc'



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
#'?video_id={}&time_offset_ms={}&end_offset_ms={}&drag_flag=0&timestamp={}&__guest_id=pc-gp-68daaba9-d178-4e59-9868-e570116d26db'
#'&__location=Japan%7CMie&__country=Japan&__cluster=aws_japan&__platform=web&__la=ja&__pcv=v2.10.25&sfr=pc&accessToken='
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site'
}
res = requests.get(url,headers=headers,params=params).json()
messages = res["body"]["models"][1]["detail"]
#print(messages[0].keys())
#print(messages[0]['time_offset_ms'])
#print(messages[-1]['time_offset_ms'])

#print(messages[0]['end_offset_ms'])
#print(messages[-1]['end_offset_ms'])

for i in range(10):
	res = requests.get(url,headers=headers,params=params).json()
	messages = res["body"]["models"][1]["detail"]
	print(messages[0]['message_id'])
	print(len(messages))
	next_time=res["body"]["models"][0]["summary"]["end_offset_ms"]				
	params['time_offset_ms'] = next_time 
	print('======')
	
	
#print(len(res["body"]["models"]['detail']))
#[1]["detail"]))
