import requests

url = "https://127.0.0.1"

files = {'file' : open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\index.html","r", encoding= 'utf-8')}

r = requests.post(url, files=files)
print(r.text)