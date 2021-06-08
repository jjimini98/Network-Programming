import threading

def prtSquare(num):
   print("Square : {}".format(num**2))

def prtCube(num):
   print("Cube : {}".format(num**3))


#위에 정의한 함수로 스레드 객체 생성
t1 = threading.Thread(target=prtSquare, args=(10,))
t2 = threading.Thread(target=prtCube, args=(10,))

#스레드 시작 
t1.start()
t2.start()

#스레드가 끝날때까지 기다리기 
t1.join()
t2.join()

print("Done!")
