import socket
import threading

IP = "127.0.0.1"
PORT = 8888


def recv_send(connection):
    while True:
        data = connection.recv(1024)
        connection.send(data)


def main():
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.bind((IP, PORT))
    serversock.listen()

    while True:
        conn, addr = serversock.accept()
        thread = threading.Thread(target=recv_send, args=(conn,))
        thread.start()


if __name__ == "__main__":
    main()
