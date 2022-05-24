#[] -used fpor lists
#() -used for tuples
#{} -used for sets
fruits=["mangoes","apples","oranges","bananas"]
names=["josh","john","james","judah","peter"]
Fruits=["tomatoes","grapes","passion","guavaz"]
#append -is used to add at the end
fruits.append("cherry")
print(fruits)
#remove 
fruits.remove("bananas")
print(fruits)
#pop -remove index
fruits.pop(1)
print(fruits)
#+

#extend
fruits.extend(Fruits)
print(fruits)
lists=(fruits+names+Fruits)
print(lists)
#clear
lists.clear()
print(lists)




#TUPLES
FRuits=('apple','pinneaple','orange')
print(FRuits)
#list -converting tuple to list
new_list=list(FRuits)
print(new_list)
new_list.append("tommatoes")
print(new_list)
#tuple -converting list to tuple
new_list=tuple(FRuits)
print(new_list)
#sets -{}
fruits_5={"apple","orange","mangoes"," cherry","apple","orange"}
print(fruits_5)






