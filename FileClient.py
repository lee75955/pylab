#!/usr/bin/python3
import socket

host = '203.250.133.88'
port = 10302
buff_size = 128
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
sock.connect(server_address)

file_name = input("Enter file name : ")

try:
    sock.sendall(file_name.encode())
except Exception as e:
    print("Exception: %s" % str(e))

fd = open(file_name, 'w')
while True:
    data = sock.recv(buff_size)
    if data:
        fd.write(data.decode())
    else:
        break

fd.close()
sock.close()
