from tkinter import *
root=Tk()
#create a frame
my_label1=Label(root,text="hello world")
my_label2=Label(root,text="hello world")
#show it on screen
my_label1.grid(row=0,column=0)
my_label2.grid(row=5,column=9)
root.mainloop()
