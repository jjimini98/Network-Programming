import requests 

url = 'http://localhost:8000'
rsp = requests.get(url)
rsp2 = requests.post(url) # 501 구현되지 않음으로 뜸 

