import re
# simple class
class Dog():
    name="dog"
    def bark(self):
        print("wooof wooof")
    def get_name(self):
        print(self.name)
dog=Dog()
dog.bark()
dog.name="alex"
dog.get_name()
# using constructor and setter / getter
class Cat():
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


