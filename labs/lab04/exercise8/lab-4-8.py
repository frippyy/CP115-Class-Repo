distance = float(input())
afterMidnight = input()
if distance > 2:
    fare = 4 + (distance - 2) * 1.2
else:
    fare = 4
if afterMidnight == "yes":
    fare = fare + 3
print(fare)
