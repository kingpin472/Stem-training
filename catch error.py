# try ,except in python to catch errors.
try:
    value=int(input("enter a number:"))
    print(value)
except ValueError:
    print("invalid")
except ZeroDivisionError:
    print("Divided by zero")    



