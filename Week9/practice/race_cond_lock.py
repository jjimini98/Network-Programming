import threading

x = 0 

def increment():
   global x 
   x +=1 

def thread_task(lock):
   for _ in range(300000):
      lock.acquire() #스레드 동기화 
      increment()
      lock.release() #스레드 동기화 

def main_task():

   global x
   x = 0

   lock = threading.Lock() #미리 실행. 그래야 객체 생성이 가능하다. 

   t1 = threading.Thread(target=thread_task, args= (lock,))
   t2 = threading.Thread(target=thread_task, args= (lock,))

   t1.start()
   t2.start()

   t1.join()
   t2.join()

for i in range(10):
   main_task()
   print("Iteration {} : x = {}".format(i,x))