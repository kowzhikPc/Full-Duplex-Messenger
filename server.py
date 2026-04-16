import socket
import time
import tkinter as tk
import threading

def sender():
    server = socket.socket()
    server.bind(("localhost",9999))
    server.listen()
    global conn
    conn,addr = server.accept()
    while True:
        if l:
            conn.send(l[0].encode("utf-8"))
            l.clear()
        time.sleep(0.01)
    conn.close()

root = tk.Tk()
root.geometry("800x800")
root.title("server")

label= tk.Label(root,text="Chat box!")
label.pack()

textbox = tk.Text(root,width=100,height=26)
textbox.pack(padx=10,pady=4)

def sumbit():
    global l
    l = []
    a= textbox.get("1.0",tk.END)
    l.append(a)
    
sumbit()

button = tk.Button(root,text="Submit.",width=7,height=1,command=sumbit)
button.pack(side="bottom",anchor="e",padx=15,pady=15)

t = threading.Thread(target=sender,daemon=True)
t.start()
root.mainloop()
