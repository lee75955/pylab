#!/usr/bin/python3

import socket

host = ''
port = 10302
BUFF_SIZE = 128
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
sock.bind(server_address)
while True:
    print("\nsaiting for request...")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(client_address[0],client_address[1]))
    print("echo message : {}". format(message.decode()))
    data = message.decode()
    try:
        data2 = int(data)
        if (data2%2)==1:
            message2 = "홀수"
        elif (data2%2)==0:
            message2="짝수입니다"
    except ValueError:
        message2="숫자가 아닙니다"

    sock.sendto(message2.encode(), client_address)
sock.close()

