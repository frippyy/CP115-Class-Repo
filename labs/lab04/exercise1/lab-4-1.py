kwh = int(input())
if kwh > 200:
    totalBill = 80 + ((kwh - 200) * 0.75)
else:
    if kwh > 100:
        totalBill = 30 + ((kwh - 100) * 0.5)
    else:
        totalBill = kwh * 0.3
print(totalBill)
