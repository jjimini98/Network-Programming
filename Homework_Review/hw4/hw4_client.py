from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 9000))


client.send(b'Jimin Yoo')
id = client.recv((1024))
print(int.from_bytes(id,'big'))
