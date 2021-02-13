import time
from tkinter import *

root = Tk()

root.geometry("125x50+0+0")

root.configure(background="black")
root.resizable(0,0)

root.overrideredirect(1)


def start():
    text = time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(1,start)

label = Label(root,font=("ds-digital",20,'bold'),bg='black',fg='green',bd=20)
label.grid(row=0,column=1)
start()
print("done")
root.mainloop()

