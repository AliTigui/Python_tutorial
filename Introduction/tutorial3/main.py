# simple function that don't return value ortake parametre
def say_hello():
    print("hello user")
say_hello()

# function that take parametre
def hello_name(name):
    print(f"hello {name}")
hello_name("Tigui")
print("_"*20)

# function take parametre and return value
def Sum(a,b):
    return a+b
print(Sum(10,20))
print("_"*20)

# function scope
var=10
def change(a):
    b=9
    var=a
change(9)
print(var) # variable didn't change
#print(b) this will cuz error it our of scope
print("*"*20)
def real_change(a):
    global var
    var=a
real_change(11)
print(var)# now it changed
print("_"*20)

# function take arbitrary number of parametre
def hello_names(*names):
    for name in names:
        hello_name(name)
hello_names("Ali","Ahmed","Anis")
l=["cat","tiger","raven","lion"]
hello_names(*l)
print("_"*20)

# function have argument with default value
def hello_boss(boss_name="Ali"):
    hello_name(boss_name)
hello_boss()
hello_boss("machmach")
print("_"*20)

# function take arbitraty number of key value
def user_data(**data):
    for k,v in data.items():
        print(f"{k} {v}")
user_data(name="ali",grade="master",age=22)
user={"name":"hmm","grade":"bs","age":20}
user_data(**user)
print("_"*20)

# function take other function as parametre
def do_something(func):
    print("hello from do something")
    func()
    print()
do_something(say_hello)
print("_"*20)

# lambdas
do_something(lambda:print("this is lambda function"))
print("_"*20)

# Recursive function 
def power(n,base=2):
    if base==0:
        return 1
    else :
        return n*power(n,base-1)
print(f"5 to power of 2 is {power(5)}")
print(f"2 to power of 5 is {power(2,4)}")
print("_"*20)

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

@func_decorator
def hi_user():
    print("hi user")
print(hi_user())

