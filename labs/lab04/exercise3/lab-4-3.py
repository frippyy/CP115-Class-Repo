hours = int(input())
if hours > 5:
    parkingFee = hours - 5 * 3 + 6
else:
    if hours > 2:
        parkingFee = hours - 2 * 2
    else:
        parkingFee = 0
if parkingFee > 30:
    parkingFee = 30
print(parkingFee)
