import tkinter as tk
from tkinter import ttk
import requests
import time
import RPi.GPIO as GPIO
from MFRC522 import MFRC522

MIFAREReader = MFRC522.Reader(0, 0, 22)
"""
Die Funktion anmelden sollte beim Programmstart automatisch in einer
endlosschleife laufen wie für das Terminal benötigt.
Das Programm solltest du wie Christian auch in den LXDE autostart reinpacken
ein Paar der Kommentare sagen was du wo anpassen sollst damit es bei dir
Funktioniert.
"""
def anmelden():
    # scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")

    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
        UID = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
        # Hier die IP-Adresse deines Servers eingeben ohne Port
        p=requests.post('http://192.168.178.57:8000/anmelden/',data={'UID':UID})
        print(p.content)
        # Hier kommt der Name des Schülers in p.content als Antwort vom Server
        # kannst du unter ppsystem/anmelden/views.py anmelden bei der HttpResponse
        # anpassen falls gewollt
        schüler = str(p.content)[2:len(str(p.content))-1]
        willkommen.configure(text=schüler)
        win.update()
        time.sleep(1)
        willkommen.configure(text="")


win = tk.Tk()
# Auf True setzen für vollbildmodus
win.attributes('-fullscreen', False)
#app=FullScreenApp(win)
win.title("Anmelde Terminal")

ttk.Label(win, text="Guten Morgen").grid(column=0,row=0)
willkommen = ttk.Label(win, text="Schüler")
willkommen.grid(column=0, row=1)

action = ttk.Button(win, text="Send UID", command=anmelden())
action.grid(column=1, row=0)

win.mainloop()
