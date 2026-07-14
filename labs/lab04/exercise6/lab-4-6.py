minutesBefore = int(input())
membership = (input().lower == 'true')
price = 80
if minutesBefore > 30:
    price = price - 15
else:
    if minutesBefore < 0:
        price = 0
if membership == True:
    price = price * 0.85
print(price)
