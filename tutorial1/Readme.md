## Tutorial 1
in this tutorial we will work with variable and data type and how to get user input

### Types in Python
python basic types are :
    * Integer, number without floating point number
    * Float, real numbers 
    * Boolean it can be either `True` or `False`
    * String list of character
    * List it dynamic array that can store more then one value also it can store value from diferent types 
    * Tuple used to store many values but we can't change those value after we create the tuple
    * Set it used to store unique data value ib sets cant'e have deplicate
    * Dictionary used to store key value pair it same as hash map
### Dynamic typing and garbage colecting
Python is dynamic type language that mean variables type can change we can pass float to variable that was created as string  
alos it use garbage colection aproch that mean the allocation of memory is automatic programe search in memory and where it find space that we don't use it create our variables there
### Mutability
mutability mean that we can change value of variables , not all data type are mutable the mutable once are :
    * list
    * dictionary
    * set
Immutable object are :
    * Integer
    * Tuple
    * String
### Taking user input and printing
to print value to the console we use `print()` , we can take user input using `input()` this function always take input as string if we want other types we can change by passing the return value to the function that will convert to our type
#### Example :
```Python
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(f"a + b = {a+b}")
```
### Comment 
we can create comment in python using `#` this wll create single line comment , in python there is no multiple line comment
