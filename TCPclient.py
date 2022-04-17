import socket
host = '203.250.133.88'
port = 10302
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connecting to %s port %s" % server_address)
sock.connect(server_address)
cmd = 'HTTP/1.1 200 OK\n Content-Type:text/html'
sock.send(cmd)

message = input("Enter message : ")
message = bytes(message, encoding='utf-8')

try:
    sock.sendall(message)
    data = sock.recv(BUFF_SIZE)
    print("received %s" %data.decode())

except Exception as e:
    print("Exception %s" %str(e))
sock.close()

