income = float(input())
if income > 100000:
    taxRate = 0.02
else:
    if income > 50000:
        taxRate = 0.01
    else:
        taxRate = 0
totalTax = income * taxRate
print(totalTax)
