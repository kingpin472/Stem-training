other_list=[]
my_list=[2,3,5,5,6,7,8,9,8,7]

for elem in my_list:
    print(elem)
    other_list.append(elem)
    print(other_list)

my_list=[2,3,5,5,6,7,8,9,8,7]
other_list=[elem for elem in my_list if  elem%2==0]
print(other_list)

my_list=[2,3,5,5,6,7,8,9,8,7]
for x in my_list:
    print(x)
    if x%2==0:
        other_list.append(x)
print(other_list)
