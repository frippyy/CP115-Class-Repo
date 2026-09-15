current_reading = int(input())
previous_reading = int(input())

consumption = current_reading - previous_reading

if consumption > 35:
    water_cost = 26.85 + ((consumption - 35) * 1.40)
elif consumption > 20:
    water_cost = 11.4 + ((consumption - 20) * 1.03)
else:
    water_cost = consumption * 0.57

total_bill = water_cost + 10

print(consumption)
print(water_cost)
print(total_bill)
