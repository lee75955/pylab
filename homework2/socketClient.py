from socket import *
import os
import sys

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('203.250.133.88', 10302))

filename = input('vsftp>')
clientSock.sendall(filename.encode('utf-8'))

data = clientSock.recv(1024)
data_transferred = 0

if not data:
    print('파일 %s 가 서버에 존재하지 않음' %filename)
    sys.exit()

nowdir = os.getcwd()
with open(nowdir+"\\"+filename, 'wb') as f:
    try:
        while data:
            f.write(data)
            data_transferred += len(data)
            data = clientSock.recv(1024)
    except Exception as ex:
        print(ex)
print('파일 %s 받기 완료. 전송량 %d' %(filename, data_transferred))