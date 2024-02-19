import re
email="example@gmail.com"
##simple search
print(bool(re.search("h",email)))
print(bool(re.search(".*@.*",email)))
print(bool(re.search(".+@.+",email)))
print(bool(re.search(r".+@.+\.com",email)))
print(bool(re.search(r"^.+@.+\.com$", email)))
print(bool(re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email)))
print(bool(re.search(r"^\w+@\w+\.com$", email)))
print(bool(re.search(r"^\w+@\w+\.com$", email, re.IGNORECASE)))
print(bool(re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE)))


# match and catching values
name= input("What's your name? ").strip()
matches= re.search(r"^(.+), (.+)$", name)
if matches:
    last, first= matches.groups()
    name= first+ " "+last
print(f"hello, {name}")
#----------------------------------------------------------------------
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), (.+)$", name):
    name= matches.group(2)+ " "+ matches.group(1)
print(f"hello, {name}")
#--------------------------------------------
url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
#--------------------------------------------------------
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))




