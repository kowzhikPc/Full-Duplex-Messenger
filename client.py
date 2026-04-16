import socket
import tkinter as tk
import threading
import time

def recv():
    client = socket.socket()
    client.connect(("localhost",9999))
    global a
    while True:
        a = client.recv(1024).decode("utf-8")
        root.after(0,lambda: textbox.insert(tk.END,a))
        time.sleep(0.1)
root = tk.Tk()
root.geometry("300x500")
root.title("client")
label = tk.Label(root,text="Chat box!")
label.pack()

textbox = tk.Text(root,height=100,width=100)
textbox.pack(padx=10,pady=4)


t = threading.Thread(target=recv,daemon=True)
t.start()

root.mainloop()

