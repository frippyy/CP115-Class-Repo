gb = int(input())
planA = 10 + gb
if gb > 20:
    planB = 25 + ((gb - 20) * 3)
else:
    planB = 25
if planA > planB:
    bill = planB
else:
    bill = planA
print(bill)
