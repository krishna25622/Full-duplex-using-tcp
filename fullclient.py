import socket
from time import ctime
import threading

host = socket.gethostname()
sADDR = (host, 45002)
buff = 1024

cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect(sADDR)


def receive():
    while True:
        rMessage = str(cliSock.recv(buff), "utf-8")
        if not rMessage:
            print("Ending connection")
            break
        print("Server:" + rMessage)


def send():
    while True:
        sMessage = input()
        if (sMessage == 'exit'):
            cliSock.send(str.encode(sMessage))
            break
        else:
            cliSock.send(str.encode(sMessage))


t1 = threading.Thread(target=send, name=1)
t2 = threading.Thread(target=receive, name=2)

t1.start()
t2.start()