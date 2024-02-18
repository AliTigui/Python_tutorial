# Conditions 
a=int(input("Enter number : "))
if a > 0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")

# Match
user="Ali"
match user:
    case "Om":
        print("Om do not have access  to the database only for the api code.")
    case "Vishal" |"Ali":
        print("Vishal, Ali do not have access to the database ,only for the frontend code.")
    case "Rishabh":
        print("Rishabh have the access to the database")
    case _:
        print("You do not have any access to the code")

# Loops
## for loop
for i in range(10):
    print(i)

l=[4,7,9,10]
for i in l:
    print(i**2)

users=[{"name":"Ali","age":20},{"name":"Russ","age":22},{"name":"Majda","age":20}]
for i in users:
    for k,v in i.items():
        print(f"{k} : {v}")
    print("*"*10)

## while loop
while int(input("Enter number : "))!=10:
    print("wrong")

j=0
while j<10:
    j+=1
    if j<5 or j%2==0:
        print("yee")
    elif j>5 and j<=8:
        print("you")
k=0
while k<100:
    k+=1
    if k%2==0:
        continue
    else:
        print(k)
    if k>80:
        break