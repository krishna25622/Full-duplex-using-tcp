import threading
from socket import *

k = 1
i = 0


def rev(connection_socket):
    global k, i
    while k:
        sentence = connection_socket.recv(2048).decode()
        if (sentence == "exit"):
            k = 0
        print(sentence)
    i = i + 1


def sen(connection_socket):
    global k, i
    while k:
        message = input()
        if (message == "exit"):
            k = 0
        connection_socket.send(message.encode())

    i = i + 1


def main():
    server_port = 5000
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("Server is listening")
    connection_socket, address = server_socket.accept()

    ts = threading.Thread(target=sen, args=(connection_socket,))
    tr = threading.Thread(target=rev, args=(connection_socket,))
    ts.start()
    tr.start()
    while (1):
        if (i == 2):
            break
    server_socket.close()
    print("connection closed")


if __name__ == "_main_":
    main()