#p.14 race_cond_lock

import threading

x = 0 #전역변수 x 

def increment():
   global x
   x +=1 

def thread_task(lock):
   for i in range(300000):
      lock.acquire()
      increment() #임계구역 
      lock.release()

def main_task():
   global x 
   x = 0

   lock = threading.Lock() #thread_task에서 사용한 lock을 쓰기위한 객체 생성

   t1 = threading.Thread(target=thread_task, args=(lock,))
   t2 = threading.Thread(target=thread_task, args=(lock,))

   t1.start()
   t2.start()

   t1.join()
   t2.join()

for i in range(10):
   main_task()
   print("Iteration {} : {}".format(i,x))
