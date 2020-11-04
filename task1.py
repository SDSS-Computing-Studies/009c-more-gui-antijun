import tkinter as tk
from tkinter import *
import math

win = tk.Tk()
win.title("Triangle Area Calculator")
win.geometry("600x400")


def triArea():
    a = s1.get()
    c = s2.get()
    b = s3.get()
    h = hL.get()

    if h == "":
        s = (float(a) + float(b) + float(c)) / 2
        area = round(math.sqrt(s*(s - float(a)) *
                               (s - float(b))*(s - float(c))), 1)
    elif float(h) > 0:
        area = round((float(b)*float(h)) / 2, 1)

    ov.set(area)


ov = StringVar()
ov.set("")

triangle = PhotoImage(file="triangle.png")

triL = Label(win, image=triangle)

s1 = Entry(win, text="a", width=8)
s2 = Entry(win, text="b", width=8)
s3 = Entry(win, text="c", width=8)
hL = Entry(win, text="height", width=8)

inL1 = Label(win, text="Enter in as much information about the")
inL2 = Label(win, text="triangle shown and I will calculate the area")

cb = Button(win, text="Calculate!", command=triArea)
out = Label(win, textvariable=ov, font=(None, 30))

triL.place(x=50, y=0)

s1.place(x=225, y=100)
s2.place(x=435, y=130)
s3.place(x=300, y=240)
hL.place(x=355, y=115)

inL1.place(x=30, y=300)
inL2.place(x=27, y=320)

cb.place(x=270, y=308)
out.place(x=370, y=308)

win.mainloop()
