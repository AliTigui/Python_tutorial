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
