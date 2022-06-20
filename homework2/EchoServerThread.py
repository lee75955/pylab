#!/usr/bin/python3

import socket
import threading

class EchoThread(threading.Thread):

    def __init__(selfself, socket, address):
        threading.Thread.__init__(self)
        self.csocket = socket
        self.ip, self.port = address
        print("[+] New service thread for {} {}".format(self.ip, self.port))

    def run(self):
        while True:
            data = self.csocket.recv(2048)
            if data:
                self.csocket.sendall(data)
            else:
                break
        print("[-] Service thread terminated for {}".format(self.ip))

host = ''
port = 10302
BACKLOG = 5

conn_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
conn_sock.bind((host, port))
conn_sock.listen(BACKLOG)

while True:
    count = threading.active_count()
    print(count)
    print("listening for incoming requests...")
    data_sock, client_address = conn_sock.accept()

    serviceThread = EchoThread(data_sock, client_address)
    serviceThread.start()