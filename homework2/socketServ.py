#!/usr/bin/python3
from socket import *
from os.path import exists
import sys

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 10302))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속했습니다')

filename = connectionSock.recv(1024)
print('받은 데이터 : ', filename.decode('utf-8'))
 일반 문자열로 변환한다
data_transferred = 0

if not exists(filename):
    print("no file")
    sys.exit()

print("파일 %s 전송 시작" %filename)
with open(filename, 'rb') as f:
    try:
        data = f.read(1024)
        while data:
            data_transferred += connectionSock.send(data)
            data = f.read(1024)
    except Exception as ex:
        print(ex)
print("전송완료 %s, 전송량 %d" %(filename, data_transferred))
