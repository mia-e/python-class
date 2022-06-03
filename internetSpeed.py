from tkinter import *
from tkinter import messagebox
import pyspeedtest

def checker  ():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download())+" [Bytes per second]")
    messagebox.showinfo("Your download speed ", a1)

root = Tk()
root.title("INTERNET SPEED CHECKER")
root.config(bg="pink")
root.geometry("500x250")

label1 = Label(root, text= "Internet speed checker", font=("Arial", 30, "bold"), bg="lightblue").pack()
button1 = Button(root, text="Click !!", font=("Arial", 20, "bold"), bg="yellow", height=1, width=10, command=checker).pack()

root.mainloop()