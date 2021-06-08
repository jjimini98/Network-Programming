import threading

x = 0 #스레드 모두가 공유하는 전역변수 x 

def increment():
   global x 
   x +=1

def thread_task():
   for _ in range(300000):
      increment() # 전역변수 x를 계속해서 증가시키는게 목적임 . 

def main_task():
   global x
   x = 0  #전역변수를 가지고와서 0으로 초기화 

   #스레드 선언 
   t1 = threading.Thread(target=thread_task)
   t2 = threading.Thread(target=thread_task)

   t1.start()
   t2.start()

   t1.join()
   t2.join()

   print("Done!")

for i in range(10):
   main_task()
   print("Iteration {} : x = {}".format(i,x))


# race condition에 의해 값이 일정하게 나오지 않고 가변적으로 나오게 됨 -> 공유자원에 대해 여러개의 스레드가 동시에 접근하는 경우임. 
# 접근의 타이밍이나 순서 등에 의해 결과값에 영향을 주는 것을 말함.
# 공유 자원에 접근하는 프로그램의 부분을 바로 임계구역(critical section)이라고 함.
