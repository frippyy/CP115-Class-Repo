income = float(input())
if income > 100000:
    totalTax = ((income - 100000) * 0.02) + 500
else:
    if income > 50000:
        totalTax = (income - 50000) * 0.01
    else:
        totalTax = 0
print(totalTax)
