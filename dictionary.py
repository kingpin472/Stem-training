#dictionaries in python
my_dict={ 
    "book":"dynamics",
    "publisher":"longhorn",
    "year":2001,
}

#accessing item
x=my_dict ["year"]
print(x)

#accessing using get()
y=my_dict["year"]
print(y)

#all keys
x=my_dict.keys()
print(x)

#all values
x=my_dict.values()
print(x)

#printing all items in a dictionary
x=my_dict.items()
print(x)
#checking if keys exist
if "publisher" in my_dict:
    print("publisher is one of the keys")









