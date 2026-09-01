name = input()
password = input()
origin = input()
destination = input()

username = name.lower()
name_length = len(name)

if len(password) >= 8:
    long_enough = True
else:
    long_enough = False

route = origin.upper() + "-" + destination.upper()

print(username)
print(name_length)
print(long_enough)
print(route)

