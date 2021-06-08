from urllib import parse

url = "http://localhost:8888/index.html?status=on"


parsed_path = parse.urlparse(url)
print(parsed_path)
real_path = parsed_path.query
query = parse.parse_qs(real_path)
print(query)