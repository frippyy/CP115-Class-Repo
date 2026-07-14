distance = float(input())
afterMidnight = (input().lower == 'true')
if distance > 2:
    fare = 8 + (distance - 2) * 1.2
else:
    fare = distance * 4
if afterMidnight == True:
    fare = fare + 3
print(fare)
