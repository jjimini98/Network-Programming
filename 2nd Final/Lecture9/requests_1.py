import requests

rsp = requests.get("https://naver.com")
print(rsp.status_code)
print(rsp.encoding) #응답데이터의 인코딩 방식

url = 'https://search.naver.com/search.naver'
payload = {'query':'iot'} # ?query=iot로 날아감 검색창에 iot라고 검색하는 것과 같음
rsp = requests.get(url,params=payload)
print(rsp.url)
print(rsp.headers)
print(rsp.text)
