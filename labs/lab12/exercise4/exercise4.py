minutes = int(input())

total_minutes = 0
customers = 0
while total_minutes < 60:
    total_minutes += minutes
    customers += 1
    if total_minutes >= 60:
        break
    minutes = int(input())

print(customers)
print(total_minutes)
