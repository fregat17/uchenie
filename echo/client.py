import socket


clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(("127.0.0.1", 8888))
print("connected")

index = 0
while True:
    print("sending data")
    clientsock.send(b'chel')
    print("data sent")
    data = clientsock.recv(1024)
    print(f'{index}Echoing: ', data)
    index += 1
