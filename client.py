import socket
import threading

client = socket.socket()
client.connect(("localhost",9999))
def sender():
    while True:
        x = input("Enter something to send-")
        if x:
            client.send(x.encode("utf-8"))
            client.send("65451465434656".encode())

def receiver():
    while True:
        data = client.recv(1024).decode("utf-8")
        if data:
            print(data)

t = threading.Thread(target=receiver,daemon=True)
t2 = threading.Thread(target=sender,daemon=True)

t.start()
t2.start()
t.join()
t2.join()   