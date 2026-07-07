weight = int(input())
ticketPrice = int(input())
if weight == 0:
    finalPrice = ticketPrice - 10
else:
    if weight > 15:
        finalPrice = ticketPrice + weight - 15 * 4
    else:
        finalPrice = ticketPrice
print(finalPrice)
