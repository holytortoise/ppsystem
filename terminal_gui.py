import tkinter as tk
from tkinter import ttk
import requests
import time
UID=101010

def anmelden():
    p=requests.post('http://192.168.178.57:8000/anmelden/',data={'UID':UID})
    willkommen.configure(text=p.content)
    time.sleep(1)
    willkommen.configure(text="")

win = tk.Tk()

win.title("Anmelde Terminal")

ttk.Label(win, text="Guten Morgen").grid(column=0,row=0)
willkommen = ttk.Label(win, text="")
willkommen.grid(column=0, row=1)

action = ttk.Button(win, text="Send UID", command=anmelden)
action.grid(column=1, row=0)

win.mainloop()
