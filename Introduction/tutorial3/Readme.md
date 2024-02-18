## Tutorial 3
This tutorial will be about functional programming

### Creating and working with function
we can create function using the `def` and after it we provide the function name and parenthese we put inside them the parametres that the function should take then if we want to make the function return value we return it using the `return` keyword
#### Example 
```Python
#function don't return value and don't take argument
def say_hello():
    print("hello user")
say_hello()

#function take argument and don't return value
def hello_name(name):
    print(f"hello {name}")
hello_name("Tigui")
print("_"*20)

#function take argument and  return value
def Sum(a,b):
    return a+b
print(Sum(10,20))
```

### Variables Scope
variable scope is where we can use our variables , if we create variable inside a function we can't use it inside the function that will cuz error   
also if we try to change variable inside function the effect will be lost when we return from the function call cuz when we do that python will just create local variable and use it , to fix that we use the `global` keyword
#### Example 
```Python
var=10
def change(a):
    b=9
    var=a
change(9)
print(var) # variable didn't change
#print(b) this will cuz error it our of scope

def real_change(a):
    global var
    var=a
real_change(11)
print(var)# now it changed
```

### function with default value and lambda function
we can set default value to function parametre just by assign default value to the parametre and if we didn't pass argument to function it will use this default value  
Lambda function are anonymous function that we create in the fly to do specific task , it better then creating function that we will use only once we create lambda function using `lambda` keyword
#### Example 
```Python
# function with default value
def hello_boss(boss_name="Ali"):
    hello_name(boss_name)
hello_boss()
hello_boss("machmach")

# lambda funtcion
lambda e: e+1
``` 

### function with arbitrary number of parametre and arbitrarynumber of key value parametre
we can create function that accept arbitrary number of paramatre by adding * to parametre name those parametre will be stored as list we can then iterate over them  
we can also create function that accept arbitrary number of key value parametre using `\*\*` those parametres will be stored as dictionary
#### Example 
```Python
# function take arbitrary number of parametre
def hello_names(*names):
    for name in names:
        hello_name(name)
hello_names("Ali","Ahmed","Anis")
l=["cat","tiger","raven","lion"]
hello_names(*l)

# function take arbitraty number of key value
def user_data(**data):
    for k,v in data.items():
        print(f"{k} {v}")
user_data(name="ali",grade="master",age=22)
user={"name":"hmm","grade":"bs","age":20}
user_data(**user)
```

### Recursive function
Recursive function are type of function that keep calling theirself again and again untill condition  become true this aproche better then using loops cuz it faster but we have to be carefull and determine the base condition of the function cuz we can get stack overflow if we keep calling the function again and again and again 
#### Example
```Python
def power(n,base=2):
    if base==0:
        return 1
    else :
        return n*power(n,base-1)
print(f"5 to power of 2 is {power(5)}")
print(f"2 to power of 5 is {power(2,4)}")
print("_"*20)
```
### function that take other function as parametre and function that return function (decorator)
python support functional programming concept we can make function that take other function as parametre and function that take return function  
also python introduce decorator to help us work with that concept and make code more clean 
#### Example 
```Python
# function take other function as parametre
def do_something(func):
    print("hello from do something")
    func()
    print()
do_something(say_hello)

# Function that return function
def func_builder():
    print("building function")
    def func():
        secret_number=10
        return 10
    return func
a=func_builder()
print(a())
print("*"*20)

def func_decorator(fn):
    print("decorating function")
    def func():
        print("hello function get decorated")
        fn()
        return "done"
    return func
fun=func_decorator(say_hello)
print(fun())
print("*"*20)
# using decorator
@func_decorator
def hi_user():
    print("hi user")
print(hi_user())
print("*"*20)

@func_decorator
def hi_user2():
    say_hello()
print(hi_user2())
hi_user2()
```
### Function documentation 
we don't have to tell function type of parametres or return values but it good practice and help others to understand how to use the function 
#### Example
```Python
def add(a:int,b:int)->int :
    return a+b

print(add(5,4))
```
### Functional programming concepts
#### Pure functions
These functions have two main properties. 
* they always produce the same output for same arguments irrespective of anything else. 
* they have no side-effects i.e. they do not modify any arguments or local/global variables or input/output streams. 
* they have immutability. The pure function’s only result is the value it returns. They are deterministic.
#### Recursive function
Iteration in functional languages is implemented through recursion. Recursive functions repeatedly call themselves, until it reaches the base case. 
#### First-Class functions and can be Higher-Order function
First-class functions are treated as first-class variable. The first class variables can be passed to functions as parameter, can be returned from functions or stored in data structures.  
Higher order functions are the functions that take other functions as arguments and they can also return functions. 
#### Referential transparency 
In functional programs variables once defined do not change their value throughout the program. Functional programs do not have assignment statements. If we have to store some value, we define new variables instead. This eliminates any chances of side effects because any variable can be replaced with its actual value at any point of execution. State of any variable is constant at any instant.
#### Variables are Immutable
In functional programming, we can’t modify a variable after it’s been initialized. We can create new variables – but we can’t modify existing variables, and this really helps to maintain state throughout the runtime of a program. Once we create a variable and set its value, we can have full confidence knowing that the value of that variable will never change.  