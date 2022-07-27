import socket

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(("127.0.0.1", 8888))

while True:
    message = input('Message: ')
    clientsock.send(message.encode('ascii'))
    data = clientsock.recv(1024)
    print('Server answers: ', data)

    ans = input('\nContinue? (y/n) :')
    if ans == 'y':
        continue
    else:
        break

clientsock.close()
