## Tutorial 7
This tutorial will see Object Oriented programming in python 
### introduction
oop is one of important coding strategy and almost used everywhere it help to make the code simples and hide all complex details
### creating class
to create class in python we use the keyword `class` then the name of the class, we can create constructor for class by creating a function ``__init__()`` inside it and this will be used everytime we create object fro the class, and after this methode we can ceate as much methods we want for the class to use 
#### Example
```Python
class Cat:
    def __init__(self,name,age):
        self.set_age(age)
        self.set_name(name)
    def talk(self):
        print("meow "*3)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,age):
        if age>0 and age <30:
            self.age=age
        else:
            raise ValueError("cat can't ahve this age ")
    def set_name(self,name):
        if re.search(r"\W",name) or not name.isalpha():
            raise ValueError("invalide name for cat")
        else:
            self.name=name
mycat=Cat("catos",10)
mycat.talk()
print(f"{mycat.get_name()} is {mycat.get_age()} year old")
```
### Inheriting in python and private attribute
in python there is no way to creat private arrtibute but when we want do so we just create attribue and then in it's name we use `__` that will meane that we ant this attribute to be private , but python don't stop us if we want access to it 