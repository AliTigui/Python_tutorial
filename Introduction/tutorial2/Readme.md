## Tutorial 2
in this tutorial we will work with control flow and loops

### If elif else
we use if else statments to control how our programe should behave depend on some conditions we can have many branch depend on our situation  
we can some many condition together using logical operator  `and` `or` `not`

#### Example
```Python
if a > 0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
```
### Match
we use the match statement to match a variable with defferent case , it same as switch cas in C but it accept more data types  
it we want combine many value in one case we separate them using | 
#### Example
```Python
user="Ali"
match user:
    case "Om":
        print("Om do not have access  to the database only for the api code.")
    case "Vishal" |"Ali":
        print("Vishal, Ali do not have access to the database ,only for the frontend code.")
    case "Rishabh":
        print("Rishabh have the access to the database")
    case _:
        print("You do not have any access to the code")
```
### Loops
we use loops to repeat block of codes there is only 2 loops in python 
#### for loop
we use for loop when we know how many times we want excute the block of code , we can use it also to iterate over collection of data
##### Example
```Python
# repeat branch of code 
for i in range(10):
    print(i)
# iterate over list
l=[4,7,9,10]
for i in l:
    print(i**2)
# iterate over list and dictionary
users=[{"name":"Ali","age":20},{"name":"Russ","age":22},{"name":"Majda","age":20}]
for i in users:
    for k,v in i.items():
        print(f"{k} : {v}")
    print("*"*10)
```
#### while loop
we use while loop when we repetation of a fonctionality or branch of code is based over condition so we don't know how much we will repeat this statements  
##### Example
```Python
while int(input("Enter number : "))!=10:
    print("wrong")
```
### break and continue
break and continue add more control to use on how the loops , break used to quit the loop , while continue used to skip the iteration