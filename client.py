import socket
import threading

client = socket.socket()
client.connect(("localhost",9999))
def sender():
    while True:
        x = input("Enter something to send-")
        client.send(x.encode("utf-8"))
        
def receiver():
    while True:
        print(client.recv(1024).decode("utf-8"))

t = threading.Thread(target=receiver,daemon=True)
t2 = threading.Thread(target=sender,daemon=True)
t.start()
t2.start()
t.join()
t2.join()