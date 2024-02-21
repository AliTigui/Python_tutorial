import re
from datetime import date
# simple class
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
# using constructor and basic setter and getter
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

# class Inheriting in python and private attribute
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

# Class decorator and working with setter and getter

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


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(20)
# classmethod/static method 
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

#operator overloading
class Complexe:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,other):
        return Complexe(self.real+other.real,self.imaginary+other.imaginary)
        self.imaginary+=other.imaginary
    def __str__(self):
        return f"{self.real}, {self.imaginary} i"
a=Complexe(4,5)
b=Complexe(6,7)
c=a+b
print(c)