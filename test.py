import pyglet
import time
from tkinter import *
from tkinter import ttk
import application

root = Tk()
root.title("Auto Timesheet")

def Set():
    setTime = entry.get()
    Current = time.strftime("%H:%M")

    while setTime != Current:
        Current = time.strftime("%H:%M")
        time.sleep(1)
    if setTime == Current:
        application.Run()

frame = ttk.Frame(root)
frame.pack()
frame.config(height=200, width=200)

label = ttk.Label(frame, text="Alarm Clock :")
label.pack()

entry = ttk.Entry(frame, width=50)
entry.pack()
entry.insert(3, "15:00")


button = ttk.Button(frame, text="Set Run time", command=Set)
button.pack()

button2 = ttk.Button(frame, text="Enter", command=Set)
button2.pack()

root.mainloop()


