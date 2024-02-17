# getting input and printing output
name = input("Enter your name : ")
age = int(input("Enter your age : "))
print(f"your name is {name} and you are {age} old")

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

# Working with Booleans
b1=True
b2=False
print(not b1)
print(b1 and b2)
print(b1 or b2)

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
print(mylist+list2)


s=set()
s.add(4)
d={"name":"ali","age":20}

