for count in range(4):
    print(count)

for number in range(10, 15):
    print(number)

for value in range(0, 25, 5):
    print(value)

for multiplier in range(1, 11):
    print(f"7 x {multiplier} = {7 * multiplier}")

week = 1
while week <= 4:
    points = int(input(f"Week {week} points: "))
    if points >= 100:
        week += 2   # skip ahead a week
    else:
        week += 1