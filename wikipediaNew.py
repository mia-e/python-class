from tkinter import *

import wikipedia as wk

window = Tk()
window.title("mini wikipedia")
window.config(bg = "light blue")
f1_heading = Frame(window)
f2_frame = Frame(window)
f3_result = Frame(window)

Label(f1_heading, text="mini wikipedia", font=("Times", 30, "bold"), bg= "lightgreen").pack(side=TOP)

Label(f2_frame, text="search here", font=("Arial", 20, "bold"), bg="green").pack(side=LEFT)

Label(f3_result, text="search results: ", font=("Ariel", 25 ,"bold"), bg="blue").pack(side=LEFT)


window.mainloop()