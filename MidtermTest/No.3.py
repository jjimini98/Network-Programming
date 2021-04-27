str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

str = str.split("?")
new_str = str[1].split("&")

dic = {}
for x in new_str:
    key, value = x.split("=")
    dic[key]=value
print(dic)