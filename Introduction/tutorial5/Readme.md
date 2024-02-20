## Tutorial 5
This tutorial will be about library and how to use others modules 

### Built in modules
built in modules are module that comme pre-installed with python we can use them with just using `import` kewyord
this technique will import all the module if we want import only 1 function we use `from module import function1,function2` also we can import everything from module using `from module import *`  
sometimes the function we want to import have same name function that we use in our code to fix that we can give alternative name to function when we import it `from module import function as func`
#### Example
```Python
import random
lucky_number=random.choice([1,2,3,4,5,6,7,8,9])
print(f"lucky number is {lucky_number}")
print(f"random number is {random.randint(0,10)}")
```

### making our modules
making our modules is easy we just create a python file and we put inside it functions that we want to use in other program
then we just import the function from the module or import all the module  
when we importing our module the interepter excute all code inside it , to avoid it we put all the code inside main function and we add condition check where we excuting the module file it if main we excute if no we don't
#### Example
```Python
def say_hello():
    print("hello")
def greet_name(name):
    print(f"hello {name}")

def main():
    say_hello()
    greet_name("Ali")

if __name__=="__main__":
    main()
```
### Installing external modules
python come with lot of built in modules but that can't be enough  we can make module for that but it can be hard working and also someone else did it , best solution is searching python package online manager and see if modules that can help us to fix our problem exist or no, the most famous package manager is pip we can install package using pip with the command `pip install package_name`  
with pip packages will be installed in the system that mean we can use them in any python project in the computer but sometimes that create problems cuz some project may need older version of package and some need newer version, better then doing that we can create virtual envirenment for the project and install package on it we do that using `python -m venv /path/to/new/virtual/environment` this will create the virtual envirenment then to activate it we just run the bat file  `\Scripts\activate.bat` to disactivate it we use `deactivate`
then we can install module using `pip install` it will install package only to the virtual envirenment  
we can see below some of pip commande
* `pip install ...` to install package or module
* `pip uninstall ...` to uninstal package or module
* `pip list` to list all installed modules and packages
* `pip freeze` to list all installed packages and modules with their version
we can install modules using requirement.txt file using `pip install requirement.txt`  
if we want to salve the installed package or modules that project in our envirenment depend on we can use `pip freeze > requirement.txt`
### command line argument
sometimes in our programme we need to include comand line argument to do that we need import the sys module and we access those argument using `sys.argv` it list that have all the arguments we passed to the command starting with the name of the script file at index 0