str="Hello guys, Welcome back to my class"
for x in str:
    if x=='l':
        continue
    else:
        print(x)

str="Hello guys, Welcome back to my class"
outstr=""
for x in str:
    if x !='l':
        outstr +=x
print(outstr)


# range
for i in range(1,15,2):
    print(i)