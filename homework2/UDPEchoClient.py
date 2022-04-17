import socket

host = '203.250.133.88'
port = 10302
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_address = (host, port)
message = input("Enter message : ")
message = bytes(message, encoding = 'utf-8')

try:
    bytes_sent = sock.sendto(message, server_address)
    data, address = sock.recvfrom(BUFF_SIZE)
    print("receive : {}".format(data.decode()))


except Exception as e:
    print("%s은 숫자가 아닙니다" %str(e))

sock.close()