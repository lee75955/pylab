#!/usr/bin/python3
import socket
host = ''
port = 10302
BUFF_SIZE = 4096
BACKLOG = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_address = (host,port)
sock.bind(server_address)
sock.listen(BACKLOG)

while True:
    print("waiting for requests...")
    data_sock, address = sock.accept()
    print("echo request from {} port {}".format(address[0],address[1]))

    message=data_sock.recv(BUFF_SIZE)

    if message:
        print(message.decode())
        html = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<HTML><BODY><H1>Hello,World!</H1></BODY></HTML>"
        try:
            data_sock.sendall(html.encode())
        except:
            pass
    data_sock.close()

sock.close()
