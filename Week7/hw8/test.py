from collections import deque
from collections import defaultdict

deq = deque()
dic_msg = {} 

msg = 'send 1 hello'
msg = msg.split(" ")  
print(msg)  
# lis = lis.append
# dic_msg[msg[1]]= lis.append(msg[2])
dic_msg[msg[1]] = deq 
deq.append(msg[2])

print(dic_msg)