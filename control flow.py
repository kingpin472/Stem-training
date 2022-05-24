#if statement
x=4
if x>=1:
    print("done")
    x-=1
print("done")
#else statement
x=2
if x==10:
    print(x)
else:
    print("not 10")
#elif to creat a grading system
grade=int(input("write students score")) 
if grade>79 and grade<101:
    print("student got A")   
if grade>69 and grade<80:
    print("student got B")
if grade>49 and grade<70:
    print("student got C")
if grade>