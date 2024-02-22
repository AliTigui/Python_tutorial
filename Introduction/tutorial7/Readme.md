## Tutorial 7
This tutorial will see Object Oriented programming in python 
### introduction
oop is one of important coding strategy and almost used everywhere it help to make the code simples and hide all complex details
### creating class
to create class in python we use the keyword `class` then the name of the class, we can make class accept constructor by creating a function ``__init__()`` inside it and this will be used everytime we create object fro the class, and after this methode we can ceate as much methods we want for the class to use 
#### Example
```Python
class Dog:
    name="dog"
    def bark(self):
        print("wooof wooof")
    def get_name(self):
        print(self.name)
dog=Dog()
dog.bark()
dog.name="alex"
dog.get_name()
```