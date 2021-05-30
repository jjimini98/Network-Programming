#

from socket import *
import threading

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))



data = sock.recv(BUFSIZE)
print(int(data))


sock.close() 