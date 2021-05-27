#p.12 race_cond

import threading

x = 0 #전역변수 x 

def increment():
   global x
   x+=1

def thread_task():
   for _ in range(300000):
      increment()

def main_task():
   global x 
   x = 0 

   t1 = threading.Thread(target=thread_task)
   t2 = threading.Thread(target=thread_task)

   t1.start()
   t2.start()

   t1.join()
   t2.join()

for i in range(10):
   main_task()
   print("Iteration {}: x = {}".format(i,x))
