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
Python also supports Inheriting: If we want to inherit from class, we just write the father's name inside the parentheses of the children. Then we can override the function or just modify them by calling the function from the parent class using `super()`.
#### Example
```Python
class Robot():
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
        self.orientation=0
        self._step=1
    def turn_clockWise(self):
        self.orientation += 90
        if self.orientation==360:
            self.orientation=0
    def turn_antiClockWise(self):
        
        self.orientation -= 90
        if self.orientation<0:
            self.orientation=270
    def walk(self,):
        if self.orientation == 0 or self.orientation % 360 == 0:
           self.x+=self._step
        elif self.orientation % 270 == 0:
            self.y-=self._step
        elif self.orientation % 180 == 0:
            self.x-=self._step
        elif self.orientation % 90 == 0:
            self.y+=self._step
    def get_position(self):
        print(f"the robot is at ({self.x},{self.y})")
    def __str__(self):
        return "this first generation robot"

myrobot=Robot("41894",0,0)
myrobot.walk()
myrobot.turn_clockWise()    
myrobot.walk()
myrobot.get_position()

class Robot_G2(Robot):
    def __init__(self,id,x,y,charge):
        super().__init__(id,x,y)
        self.charge=charge
        self.turbo_state=False
    def turbo(self):
        if self.charge>0:
            self.turbo_state=True
        else :
            print("out of energy")
    def walk(self):
        if self.turbo_state and self.charge > 0:
            self._step=2
            self.charge-=1
        else:
            self.turbo_state=False
            self._step=1
        super().walk()
    def __str__(self):
        return "this 2 generation robot"
robot2gen=Robot_G2("4484",0,0,10)
robot2gen.turbo()
robot2gen.walk()
robot2gen.turn_antiClockWise()
robot2gen.walk()
robot2gen.turn_clockWise()
robot2gen.walk()
robot2gen.get_position()
print(robot2gen)
```
### Setter and Getter
setter and getter are methods that we use to set and get attribute from the class  
setter are useful cuz they help use to provide a condition when setting a value  
getter can be used to get value of attribute in specific format
#### Example
```Python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

```
### classmethod static method 
A class method is one that is attached to the class itself rather than the class's object it takes a class parameter that points to the class and not the object instance, they have access to the class's state.It has the ability to change a class state that would impact every instance of the class it could change a class variable that would affect all instances  
A static method is a method that is tied to the class instead of the class's object. It is not possible to pass an implicit first argument to a static method. The class state cannot be accessed or changed by this method. It is present in a class because having the method in a class makes sense.
#### Example
```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))
```
### OOp principles
#### Encapsulation
Encapsulation means to enclose data by containing it within an object. In OOP, encapsulation forms a barrier around data to protect it from the rest of the code. You can perform encapsulation by binding the data and its functions into a class. This action conceals the private details of a class and only exposes the functionality essential for interfacing with it. When a class doesn't allow direct access to its private data, it's well-encapsulated.
#### Abstraction
Abstraction refers to using simplified classes, rather than complex implementation code, to access objects. Often, it's easier to design a program when you can separate the interface of a class from its implementation. In OOP, you can abstract the implementation details of a class and present a clean, easy-to-use interface through the class member functions. Abstraction helps isolate the impact of changes made to the code so if an error occurs, the change only affects the implementation details of a class and not the outside code.
#### Inheritance
Most object-oriented languages support inheritance, which means a new class automatically inhabits the same properties and functionalities as its parent class. Inheritance allows you to organize classes into hierarchies, where a class might have one or more parent or child classes. If a class has a parent class, it means the class has inherited the properties of the parent. The child class can also modify or extend the behavior of its parent class. Inheritance allows you to reuse code without redefining the functions of a child class.
#### Polymorphism
Polymorphism refers to creating objects with shared behaviors. In OOP, polymorphism allows for the uniform treatment of classes in a hierarchy. When you write code for objects at the root of the hierarchy, any objects created by a child class within the hierarchy have the same functions. Depending on the type of object, it may execute different behaviors.