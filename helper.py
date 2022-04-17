import socket

host = '203.250.133.88'
port = 10302
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host, port)
sock.bind(server_address)

while True :
    print("\nwaiting for request.,,")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(client_address[0], client_address[1]))
    print("echo message : {}".format(message.decode()))

    sock.sendto(message, client_address)

socket.close()
