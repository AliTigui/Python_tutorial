# getting input and printing output
name = input("Enter your name : ")
age = int(input("Enter your age : "))
print(f"your name is {name} and you are {age} old")
print("_"*20)
print(" "*20)

# Working with float and Integer
a = 5
b = 2.5
print(a+b)
print(a-b)
print(a*b)
print(a*b)
print(a**2)
print(a//2)
print(a%3)
b,a=a,b
print("_"*20)
print(" "*20)

# Working with Booleans
b1=True
b2=False
print(not b1)
print(b1 and b2)
print(b1 or b2)
print("_"*20)
print(" "*20)

# Working with String
username="Ali abdelghani"
name=" Anunnake"
full_name=username+name
print(username.title())
print(username.upper())
print(username.lower())
print(username.split())
print(username[1:-4])
print(username[0])
print(full_name)
print("#"*5)
print("ali".center(10,"_"))
print("_"*20)
print(" "*20)

# Working with List and Tuple
mylist=[]
mylist.append(4)
mylist.append(10)
mylist.append(11)
mylist.append(12)
print(mylist)
print(mylist.pop())
print(mylist)
print(f"first value of the list {mylist[0]}")
print(f"is {4} in the list {4 in mylist}")
mylist.remove(10)
print(mylist)
mylist.sort()
mylist.reverse()
list2=[1,2,3,4,5]
list2[0]=88
print(mylist+list2)
my2Dlist=[[1,2],[4,5],[6,7],[8,9]]
print(len(my2Dlist))
print(my2Dlist[0])
print(my2Dlist[0][1])
lc=[i for i in range(10)]# list comprehention
lc2d=[[j,i] for j in range(4) for i in range(5)]  
print(lc2d)
t=(4,5,7)
print(t[0])
(a,*b)=lc
print(a)
print(b)
print("_"*20)
print(" "*20)

# Set Dictionary
empty_set=set()
set1={4,5,7,9,10,11}
set2={1,2,3,4,5}
set1.add(6)
set1.remove(10)
print(f"union of {set1} and {set2} is {set1.union(set2)}")
print(f"difference between of {set1} and {set2} is {set1.difference(set2)}")
print(f"symmetric difference between of {set1} and {set2} is {set1.symmetric_difference(set2)}")
print(f"intersection between of {set1} and {set2} is {set1.intersection(set2)}")
print("_"*20)
print(" "*20)

# Dictionary
dictionary={} 
dictionary.setdefault("name","ali")
dictionary["age"]=20
print(dictionary)
dictionary.update(name="anunnaki")
print(dictionary.pop("age"))
print(dictionary.items())
print(dictionary.keys())

