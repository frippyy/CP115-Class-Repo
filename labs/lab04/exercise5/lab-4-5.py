scoreA = int(input())
scoreB = int(input())
if scoreA > scoreB:
    pointsA = 3
    pointsB = 0
else:
    if scoreB > scoreA:
        pointsA = 0
        pointsB = 3
    else:
        pointsA = 1
        pointsB = 1
if scoreA == 0:
    pointsB = pointsB + 1
if scoreB == 0:
    pointsA = pointsA + 1
print(pointsA)
print(pointsB)
