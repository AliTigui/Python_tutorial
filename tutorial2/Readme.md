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