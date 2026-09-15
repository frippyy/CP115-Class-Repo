tempRoom = float(input())
tempTarget = float(input())
if tempRoom < tempTarget:
    power = (tempTarget - tempRoom) * 10
else:
    if tempRoom > tempTarget:
        power = (tempRoom - tempTarget) * 8
    else:
        power = 0
if power > 100:
    power = 100
print(power)
