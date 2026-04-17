import socket
import tkinter as tk
import threading
import time
import sys

def recv():
    global client
    client = socket.socket()
    client.connect(("localhost",9999))
    global a
    i = 1
    while True:
        a = client.recv(2048).decode()
        textbox.config(state="normal")
        textbox.insert(tk.END,time.asctime()[11:-8]+" : "+a+"\n")
        textbox.config(state="disabled")
def sender():
    x = entry.get()
    entry.delete(0,tk.END)
    client.send(x.encode("utf-8"))
    textbox.config(state="normal")
    textbox.insert(tk.END,time.asctime()[11:-8]+" : "+x+"\n")
    textbox.config(state="disabled")

def exiter():
    client.send("32@34".encode("utf-8"))
    client.close()
    sys.exit(0)

root = tk.Tk()
root.geometry("800x800")
root.title("client")
root.config(background="black")

label= tk.Label(root,text="Chat box!",foreground="black",background="#21d40d")
label.pack()

textbox = tk.Text(root,width=100,height=34,background="#bdc4bb",state="disabled")
textbox.pack(padx=10,pady=4)

entry = tk.Entry(root,width=114)
entry.pack(side="right",anchor="n",padx=10,pady=8)

button = tk.Button(root,text="Send",width=10,height=1,command=sender)
button.place(x=700,y=760)

button2 = tk.Button(root,text="Exit Chat!",width=10,height=1,command=exiter)
button2.place(x=600,y=760)
label2 = tk.Label(root,text="Type to Send :")
label2.place(x=10,y=584.3,)

t = threading.Thread(target=recv,daemon=True)
t.start()

root.mainloop()

