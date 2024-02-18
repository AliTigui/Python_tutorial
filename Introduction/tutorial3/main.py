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
