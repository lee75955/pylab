#!/usr/bin/python3
import socket
import sys
import os
import signal
import errno
import subprocess
from urllib.parse import urlparse

phrase = {'200':'OK', '404':'File Not Found',
          '500':'Internal Server Error', '501': 'Not Implemented'}
            #200, 500, 501 오류 정의

'''서버가 꺼졌을 때 출력하는 함수이다.'''
def shutdownServer(signum, frame):
    print("server shutdown ...")
    sys.exit(0)

'''시그널 핼들러가 발생했을 떄 실행하고 waitpid를 사용하여 종료된 자식 프로세스들을
좀비 상태에서 제거한다.'''
def collectZombie(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                break
        except:
            break
'''파일이름을 알면 파일이름을 읽어 반환하는 함수이고 만약 오류가 생기면 오류메시지를 전송한다.'''
def getFile(fileName):
    try:
        reqFile = open(fileName, 'r')
        code = '200'
        body = reqFile.read()
    except FileNotFoundError as e:
        code = '404'
        body = '<HTML><HEAD><link rel="short icon" href="#"></HEAD>'\
                       '<BODY><H1>404 File Not Found</H1></BODY></HTML>'
    return (code, body)

'''try문을 통해 서버 프로세스를 생성하고 환경변수 넘겨준 후 PIPE와 stdout을 연결하고 
pipe byte stream을 unicode로 바꿔주고 except문을 통해 예외 상황 처리를 한다.'''
def doCGI(cgiProg, qString):
    envCGI = dict(os.environ, QUERY_STRING=qString)
    prog = './' + cgiProg
    print(prog)
    try:
        proc = subprocess.Popen([prog], env=envCGI, stdout=subprocess.PIPE)
        code = '200'
        body = proc.communicate()[0].decode() #pipe byte stream -> unicode
    except Exception as e:
        code = '500'
        body = '<HTML><HEAD><link rel="short icon" href="#"></HEAD>' \
 '<BODY><H1>500 Internal Sever Error</H1></BODY></HTML>'
        pass
    return (code, body)


'''try문에서 소켓에서 클라이언트가 보내온 메세지를 받아내고 오류가 있으면 종료시킨다.
메세지가 0이 아니면 reqMessage if문을 실행하고 그러지않다면 소켓을 종료시킨다.
메소드가 'GET'이라면 if문을 실행하고 그 외 모든것들은 501코드를 실행시킨다.'''
def doHTTPService(sock) :
    try :
        reqMessage = sock.recv(RECV_BUFF)
    except ConnectionResetError as e :
        sock.close()
        return

    if reqMessage :
        msgString = bytes.decode(reqMessage) #유니코드 형태로 변환
        print(msgString)
        lines = msgString.split('\r\n')
        reqLine = lines[0]
        fields = reqLine.split(' ')
        method = fields[0]
        reqURL = fields[1]

    else :
        sock.close()
        return

    if method == 'GET':
        r = urlparse(reqURL)
        if r.path == '/':
            fileName = 'index.html'
        else :
            fileName = r.path[1:]

        fileType = fileName.split('.')[1]

        if fileType.lower() == 'cgi': # process CGI
            code, responseBody = doCGI(fileName, r.query)
        else :   # read the requested file
            code, responseBody = getFile(fileName)

    else:
        code = '501'
        responseBody = '<HTML><HEAD><link rel="short icon" href="#"></HEAD>' \
                       '<BODY><H1>501 Method Not Implemented</H1></BODY></HTML>'
    statusLine = f'HTTP/1.1 {code} {phrase[code]}\r\n'
    headerLine1 = 'Server: vshttpd 0.1\r\n'
    headerLine2 = 'Connection: close\r\n'
    headerLine3 = f'Contents Length: {len(responseBody)}bytes\r\n\r\n'
    sock.sendall(statusLine.encode())
    sock.sendall(headerLine1.encode())
    sock.sendall(headerLine2.encode())
    sock.sendall(headerLine3.encode())
    sock.sendall(responseBody.encode())

    sock.close()

'''서버의 IP와 포트번호이다.'''
HOST_IP = '203.250.133.88'
PORT = 10303
BACKLOG = 5
RECV_BUFF = 10000

signal.signal(signal.SIGINT, shutdownServer)
signal.signal(signal.SIGCHLD, collectZombie)

'''try문을 사용하여 소켓을 연결하고 except문으로 종료한다.'''
try :
    connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except :
    print("failed to create a socket")
    sys.exit(1)

'''try문으로 호스트 ip와 포트번호를 bind하고 except문을 이용해 실패 메시지를남기고 종료한다.'''
try:  # user provided port may be unavaivable
    connSock.bind((HOST_IP, PORT))
except Exception as e:
    print("failed to acquire sockets for port {}".format(PORT))
    sys.exit(1)

print("server running on port {}".format(PORT))
print("press Ctrl+C (or $kill -2 pid) to shutdown the server")

connSock.listen(BACKLOG)

'''try문에서 accept함수로 대기열에 연결 요청된 새로운 소켓을 반환하고
except문에서 오류코드에 따라 if else 문을 실행하고
pid는 자식으로서 conn.socket과 dataSock의 값을 그대로 넘겨받는다.'''
while True:
    print("waiting a new connection...")
    try :
        dataSock, addr = connSock.accept()
        print("got a connection request from: {}".format(addr))
    except IOError as e :
        code, msg = e.args
        if code == errno.EINTR:
            continue
        else:
            raise

    pid = os.fork()
    if pid == 0:
        doHTTPService(dataSock)
        sys.exit(0)

    dataSock.close()

