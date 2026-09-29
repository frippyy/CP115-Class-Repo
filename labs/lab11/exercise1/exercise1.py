speed = int(input())

total_readings = 0
longest_streak = 0
streak = 0
while speed >= 0:
    total_readings += 1
    if speed < 20:
        streak += 1
    else:
        if streak > longest_streak:
            longest_streak = streak
        streak = 0
    speed = int(input())

if streak > longest_streak:
    longest_streak = streak

print(total_readings)
print(longest_streak)
