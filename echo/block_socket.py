import socket
import threading

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(("127.0.0.1", 8888))
serversock.listen()

lock = threading.Lock()


def recv_send(connection):
    while True:
        data = connection.recv(1024)
        connection.send(data)


while True:
    conn, addr = serversock.accept()
    thread = threading.Thread(target=recv_send, args=(conn,))
    thread.start()
