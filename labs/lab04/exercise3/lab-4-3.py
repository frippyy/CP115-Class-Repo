hours = int(input())
if hours > 5:
    parkingFee = hours * 3
else:
    if hours > 2:
        parkingFee = hours * 2
    else:
        parkingFee = 0
if parkingFee > 30:
    parkingFee = 30
print(parkingFee)
