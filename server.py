import socket
import threading
import time

server = socket.socket()

server.bind(("localhost",9999))

server.listen()


conn,addr = server.accept()

def Receiver():
    while True:
        data = conn.recv(1024).decode("utf-8")
        if data:
            if data != "65451465434656":
                print(data)
            else:
                x = input("Enter something to Send-")
                conn.send(x.encode("utf-8"))

             
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
