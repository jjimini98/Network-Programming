import requests
import re

url = 'https://labs.sch.ac.kr/department/iot/01.php#department-professorS'

rsp = requests.get(url)
html = rsp.text
result = re.findall(r'([a-z0-9]+)(@sch.ac.kr)',html)

for x in result:
    res = ''.join(x)
    print(res)
