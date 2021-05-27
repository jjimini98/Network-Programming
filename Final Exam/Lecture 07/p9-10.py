#p.9-10 simple_thread_class 

import threading
import datetime

class myThread(threading.Thread):
   def __init__(self,name,counter): 
      super().__init__()
      self.name = name
      self.counter = counter

   def run(self):
      print("\n Starting {}[{}]".format(self.name, self.counter))
      myThread.print_date(self.name, self.counter)
      print("\n Existing {}[{}]".format(self.name, self.counter))

      
   def print_date(threadName, counter):
      today = datetime.date.today()
      print("\n {} [{}] : {}".format(threadName,counter,today))


thread1 = myThread('th',1) #myThread 함수 안에 init 보면 인자로 두 개를 받기 때문에 객체를 생성할 때 인자를 꼭 두 개 넣어준다. 
thread2 = myThread('th',2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("\n Exiting the program")
