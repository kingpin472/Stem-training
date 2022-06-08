from tkinter import *
root=Tk()
def click():
    my_label=Label(root,text="hey you clicked!")
    my_label.pack()
B=Button(root,text="click me",command=click,fg="blue")
B.pack()
root.mainloop() 






















