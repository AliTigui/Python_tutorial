## Tutorial 4
This tutorial will be about exceptions and errors and reading from files

### Error handling
there is 2 type of errors that we can get in our programming journey , syntexe type error those type of errors are made by use those types of error will make our programme crash when we run it there is no way to prevent them from crashing the system . we have to fix them manualy by checking our code, the second type of errors are runtime errors those are resulted by unexcepted scenario like user enter not valide data etc we can't handel those types of errors but we can make our programe cash them that will prevent our system from crashing  
To handel runtimes error we use `try` `except` we put the code that we know it may cuz error inside `try` block then we use `except` to except erros we can specific type of error after the except that make our system behave in different way depends in each errors or we can make empty except that will cash all errors  
after catching errors we can add `else` code inside it will run when there is no errors and we can also add `finally` code inside it will run no matter if there was error or no 
#### Example :
```Python
try :
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(f"result is {divide(a,b)}")
except ZeroDivisionError:
    print("number 2 shouldn't be 0")

except TypeError:
    print("Input should be number ")
except :
    print("Other Errors")
else :
    print("Everything worked well")
finally:
    print("Hope it worked for you")
```
### Raising error
sometimes we want to raise error even if everything fine for example we want only positive value and we gate negative one , we do that by using the `raise` keyword then after it we chose typeof error that we want to raise and we pass inside it string to display to the user
#### Example
```Python
try :
    a = int(input("Enter odd number: "))
    if a % 2 != 0:
        raise Exception("You most to enter odd number")
except :
    pass
else:
    print(f"{a} /2 is {a/2}")
finally:
    print("Programe ended")
```

### Writing and reading from files
story data only in memory not good cuz we can run out of memory also when we shut down our pc we will lose it to fix that we can store them to file, working with file in python is easy but before doing that we need to understand the modes of oppening file
* w this mean writting to the file this method overwrite the file we lose data that we had in file and we write new one
* a append it used to writing to the file but here we just append new data we don't overwrite it 
* r it used to open file in reading mode
there is 2 approch of openning file we can use the old style using the `open` and `close` methodes or we can use the modern aproche using the `with` `as` kewyord 
#### Example
```Python
name = input("What's your name? ")
file = open("names.txt", "w")
file.writelines([f"{name}\n","MAjda\n"])
file.close()

name = input("What's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
    
# read from file
with open("names.txt") as file:
    lines = file.readlines()
for line in lines:
    print("hello,", line.rstrip())
## other aproch in reading
with open("names.txt") as file:
    for line in file: 
        print("hello,", line.rstrip())

```