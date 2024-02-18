import random
import sys
from utility import say_hello
from utility import greet_name as gname
# working with moduls
lucky_number=random.choice([1,2,3,4,5,6,7,8,9])
print(f"lucky number is {lucky_number}")
print(f"random number is {random.randint(0,10)}")
numbers=[i for i in range(10)]
random.shuffle(numbers)
print(numbers[0])
print(sys.argv[1])
say_hello()
gname("Majda")

#Regular expression