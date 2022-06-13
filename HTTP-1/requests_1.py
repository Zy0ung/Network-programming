import requests

rsp = requests.get('https://naver.com')
print(rsp.status_code)
print(rsp.encoding)

url = 'https://search.naver.com/serach.naver'
payload = {'query': 'IoT'}
rsp = requests.get(url, params=payload)
print(rsp.url) # 요청 URL
print(rsp.headers) # 응답 헤더
print(rsp.text[:1000]) # 응답 데이터