
from tkinter import *
root=Tk()
#creating a text feild space
e1=Entry(root,width=100,bg="black",fg="green")
e1.pack()
e1.insert(0,"Enter first namber:")
#second input
e2=Entry(root,width=50,bg="black",fg="green")
e2.pack()
e2.insert(0,"Enter second number:")

#creating a task function
def click():
    num1=float(e1.get())
    num2=float(e2.get())
    add=num1+num2
    sub=num1-num2
    div=num1/num2
    mult=num1*num2
    Ans="add : "+str(add)+"\nsub :"+str(sub)+"\ndiv: "+str(div)+"\nmult : "+str(mult)
    my_label=Label(root,text=Ans)
    my_label.pack()
B=Button(root,text="=",command=click,fg="blue")
B.pack()
root.mainloop() 











