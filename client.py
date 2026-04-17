import socket
import tkinter as tk
import threading
import time

def recv():
    client = socket.socket()
    client.connect(("localhost",9999))
    global a
    i = 1
    while True:
        a = client.recv(1024).decode()
        textbox.config(state="normal")
        textbox.insert(tk.END,time.asctime()[11:-8]+" : "+a+"\n")
        textbox.config(state="disabled")
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

button = tk.Button(root,text="Send",width=10,height=1)
button.place(x=700,y=760)

label2 = tk.Label(root,text="Type to Send :")
label2.place(x=10,y=584.3,)

t = threading.Thread(target=recv,daemon=True)
t.start()

root.mainloop()

