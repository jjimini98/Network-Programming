with open(filename, 'rb') as f:
    try:
        data = f.read(1024) #1024바이트 읽는다
        while data: #데이터가 없을 때까지
            data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
            data = f.read(1024) #1024바이트 읽음
    except Exception as ex:
        print(ex)