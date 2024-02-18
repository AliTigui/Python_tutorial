def divide(a:int,b:int) -> float:
    return a / b
# working with try except
try :
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(f"result is {divide(a,b)}")
except ZeroDivisionError:
    print("number 2 shouldn't be 0")

except TypeError:
    print("Input should be number ")
except :
    print("Other Errors")
else :
    print("Everything worked well")
finally:
    print("Hope it worked for you")
# rising our errors
try :
    a = int(input("Enter odd number: "))
    if a % 2 != 0:
        raise Exception("You most to enter odd number")
except :
    pass
else:
    print(f"{a} /2 is {a/2}")
finally:
    print("Programe ended")



# working with files
## Writes to a file 
name = input("What's your name? ")
file = open("names.txt", "w")
file.writelines([f"{name}\n","MAjda\n"])
file.close()

name = input("What's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
# read from file
with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
## other aproch in reading
with open("names.txt") as file:
    for line in file: 
        print("hello,", line.rstrip())

