import tkinter as tk
import time
import socket
import threading

def sender():
    server = socket.socket()
    server.bind(("localhost",9999))
    server.listen()
    global conn
    conn,addr = server.accept()

def sumbit():
    textbox.config(state="normal")
    textbox.insert(tk.END,time.asctime()[11:-8]+" : "+entry.get()+"\n")
    conn.send(entry.get().encode("utf-8"))
    entry.delete(0,tk.END)
    textbox.config(state='disabled')

root = tk.Tk()
root.geometry("800x800")
root.title("server")
root.config(background="black")

label= tk.Label(root,text="Chat box!",foreground="black",background="#21d40d")
label.pack()

textbox = tk.Text(root,width=100,height=34,background="#bdc4bb",state="disabled")
textbox.pack(padx=10,pady=4)

entry = tk.Entry(root,width=114)
entry.pack(side="right",anchor="n",padx=10,pady=8)

button = tk.Button(root,text="Send",width=10,height=1,command=sumbit)
button.place(x=700,y=760)

label2 = tk.Label(root,text="Type to Send :")
label2.place(x=10,y=584.3,)

t = threading.Thread(target=sender,daemon=True)
t.start()

root.mainloop()
