from tkinter import *
import os
import requests
import json


os.system("sudo service tor start")

def function():
    global function
    
    is_on = True
    man_on = PhotoImage(file="src/man_on.png")
    man_off = PhotoImage(file="src/man_off.png")
        
    start = 'anonsurf start'
    os.system(start)

    if is_on:
        Label(root, text="", bg="white", image=man_on).place(x="-13", y="-26")
        Button(text="Disconnect", bg="white", fg="Black", command=disconnect, width=13, height=1).place(x=75, y=279)
        Button(text="Change IP", bg="white", fg="Black", command=change, width=13, height=1).place(x=75, y=309)
        is_on = False
    else:
        Label(root, text="", bg="white", image=man_off).place(x="-13", y="-26")
        Button(text="Connect", bg="white", fg="Black", command=function, width=13, height=1).place(x=75, y=279)
        is_on = True
        
    os.system("anonsurf restart")    
        
    root.mainloop()
    function()


def disconnect():
    stop = 'anonsurf stop && service tor stop'
    os.system(stop)
    
    man_off = PhotoImage(file="src/man_off.png")
    Label(root, text="", bg="white", image=man_off).place(x="-13", y="-26")
    Button(text="Connect", bg="white", fg="Black", command=function, width=13, height=1).place(x=75, y=279)

    Label(root, text="Unknown", bg="white", fg="black").place(x=57, y=406)
    Button(text="Change IP", bg="white", fg="Black", command=change, width=13, height=1, state="disabled").place(x=75, y=309)
    
    root.mainloop()
    disconnect()
    
    
def change():
    change = 'anonsurf changeid'  
    os.system(change)


def screen():
    global root
    root = Tk()
    root.geometry("279x459")
    root.title("AnonVPN")
    root.configure(background="White")

    Button(text="Connect", bg="white", fg="Black", command=function, width=13, height=1).place(x=75, y=279)
    Button(text="Change IP", bg="white", fg="Black", command=change, width=13, height=1, state="disabled").place(x=75, y=309)
  
    man_off = PhotoImage(file="src/man_off.png")
    Label(root, text="", bg="white", image=man_off).place(x="-13", y="-26")
  
    Label(root, text="Unknown", bg="white", fg="black").place(x=57, y=406)
    
    world = PhotoImage(file="src/world.png")
    Label(root, text="", bg="white", image=world).place(x=10, y=397)
    
    
    root.mainloop()
screen()
