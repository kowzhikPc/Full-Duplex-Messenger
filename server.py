import socket
import threading
import time

server = socket.socket()

server.bind(("localhost",9999))

server.listen()


conn,addr = server.accept()

def Receiver():
    while True:
        print("\n",conn.recv(1024).decode("utf-8"))
    
def sender():
        while True:
            x = input("Enter something to Send-")
            conn.send(x.encode("utf-8"))

recv = threading.Thread(target=Receiver,daemon=True)
send = threading.Thread(target=sender,daemon=True)


recv.start()
send.start()
recv.join()
send.join()
