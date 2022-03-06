from tkinter import *
import os
import requests
import json



def function():
    global function
    
    is_on = True
    man_on = PhotoImage(file="src/man_on.png")
    man_off = PhotoImage(file="src/man_off.png")
    
    network_down = 'ifconfig wlan0 down && ifconfig eth0 down'
    os.system(network_down)
    
    change_mac = 'macchanger wlan0 --random && macchanger eth0 --random'
    os.system(change_mac)
    
    network_up = 'ifconfig wlan0 up && ifconfig eth0 up'
    os.system(network_up)
        
    start = 'service tor start && anonsurf start'
    os.system(start)

    if is_on:
        Label(root, text="", bg="white", image=man_on).place(x="-13", y="-26")
        Button(text="Disconnect", bg="white", fg="Black", command=disconnect, width=13, height=1).place(x=90, y=279)
        is_on = False
    else:
        Label(root, text="", bg="white", image=man_off).place(x="-13", y="-26")
        Button(text="Connect", bg="white", fg="Black", command=function, width=13, height=1).place(x=90, y=279)
        is_on = True
    
    request = requests.get('https://ipinfo.io/json')
    country = request.json()['country']
    region = request.json()['region']
    
    Label(root, text=f"{region}, {country}", bg="white", fg="black").place(x=57, y=406)
    Button(text="Change IP", bg="white", fg="Black", command=change, width=13, height=1).place(x=90, y=309)
        
    root.mainloop()
    function()
        
    
   
def disconnect():
    stop = 'anonsurf stop && service tor stop'
    os.system(stop)
    
    man_off = PhotoImage(file="src/man_off.png")
    Label(root, text="", bg="white", image=man_off).place(x="-13", y="-26")
    Button(text="Connect", bg="white", fg="Black", command=function, width=13, height=1).place(x=90, y=279)
    
    request = requests.get('https://ipinfo.io/json')
    country = request.json()['country']
    region = request.json()['region']
    
    Label(root, text=f"{region}, {country}", bg="white", fg="black").place(x=57, y=406)
    Button(text="Change IP", bg="white", fg="Black", command=change, width=13, height=1, state="disabled").place(x=90, y=309)
    
    root.mainloop()
    disconnect()
    
    
def change():
    change = 'anonsurf change'  
    os.system(change)


def screen():
    global root
    root = Tk()
    root.geometry("279x459")
    root.title("AnonVPN")
    root.configure(background="White")

    Button(text="Connect", bg="white", fg="Black", command=function, width=13, height=1).place(x=90, y=279)
    Button(text="Change IP", bg="white", fg="Black", command=change, width=13, height=1, state="disabled").place(x=90, y=309)
    
    request = requests.get('https://ipinfo.io/json')
    country = request.json()['country']
    region = request.json()['region']
  
    man_off = PhotoImage(file="src/man_off.png")
    Label(root, text="", bg="white", image=man_off).place(x="-13", y="-26")
  
    Label(root, text=f"{region}, {country}", bg="white", fg="black").place(x=57, y=406)
    
    world = PhotoImage(file="src/world.png")
    Label(root, text="", bg="white", image=world).place(x=10, y=397)
    
    
    root.mainloop()
screen()