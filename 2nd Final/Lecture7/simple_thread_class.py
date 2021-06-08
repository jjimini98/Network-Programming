import threading
import datetime

class myThread(threading.Thread):
   def __init__(self, name, counter):
      super().__init__()
      self.name = name
      self.counter = counter

   def run(self):
      print("\n Starting {} [{}]".format(self.name, self.counter))
      print_date(self.name, self.counter)
      print("\n Exiting {} [{}]".format(self.name,self.counter))


def print_date(threadName,counter):
   today = datetime.date.today()
   print("\n {} [{}] : {}".format(threadName,counter,today))

   
thread1 = myThread('Th',1)
thread2 = myThread('Th',2)
#스레드를 실행해보면 각각 스레드 별 별도의 실행흐름을 가지고 있기 때문에 순서를 우리가 항상 보장할 수 없다.

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("\n Exiting the program")