## Tutorial 2
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