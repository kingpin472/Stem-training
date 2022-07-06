#opening and editing files in python
role_file=open("roles.txt","r")
print(role_file.readline())

#close file-close
role_file.close()

#write-w
role_file=open("roles.txt","a")
role_file.write("I love myself ")
role_file.close()





