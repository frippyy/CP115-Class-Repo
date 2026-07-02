principle = float(input())
rate = float(input())
time = float(input())
interest = principle * rate * time
totalAmount = interest + principle
monthlyInterest = interest / (time * 12)
print(interest)
print(totalAmount)
print(monthlyInterest)