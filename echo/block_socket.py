import socket

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(("127.0.0.1", 8888))
serversock.listen(2)
clientsock, addr = serversock.accept()
while True:
    # clientsock, addr = serversock.accept()
    data = clientsock.recv(1024)
    clientsock.send(data)
