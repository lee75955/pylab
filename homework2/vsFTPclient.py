#!/usr/bin/python3
import socket
import sys

host = '127.0.0.1'
port = 10001

while True :
    request = input("vsftp> ")
    req_field = request.split()

    if len(req_field) == 1 :
        cmd = req_field[0]
    elif len(req_field) == 2 :
        cmd = req_field[0]
        filename = req_field[1]
    else :
        continue

    if len(req_field) == 1 :
        if cmd.upper() == 'QUIT':
            break
        else :
            print("Unknown Command... ")
            continue

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)
        sock.connect(server_address)
    except:
        print("connection failed...")
        sys.exit(0)

    if cmd.upper() == 'GET' :

        message = cmd + ' ' + filename + '\n'
        sock.sendall(message.encode())

        sd = sock.makefile('r')

        resp_line = sd.readline()
        code, phrase = resp_line.split()

        if code == '100':

            sd.readline()

            fd = open(filename, 'w')
            data = sd.readline()
            while data:
                fd.write(data)
                data = sd.readline()

            print("File Receive Success")
            fd.close()
            sd.close()

        elif code == '400':
            print("File Not Found")
        else:
            pass

    elif cmd.upper() == 'PUT':

        sdr = sock.makefile("r")
        sdw = sock.makefile("w")

        req_line = "PUT" + filename + "\n\n"

        fd = open(filename, "r")

        body = fd.read()


        sdw.write(req_line)
        sdw.write(body)

        print("File Upload completed")
        sdw.close()
        fd.close()
        sdr.close()

    sock.close()



