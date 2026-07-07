kwh = int(input())
if kwh > 200:
    rate = 0.75
else:
    if kwh > 100:
        rate = 0.5
    else:
        rate = 0.3
totalBill = kwh * rate
print(totalBill)
