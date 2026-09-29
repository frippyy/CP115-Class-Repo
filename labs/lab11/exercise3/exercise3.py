number = int(input())

count = 0
biggest_jump = 0
prev_number = number
while number != 0:
    count += 1
    jump = number - prev_number
    if jump > biggest_jump:
        biggest_jump = jump
    prev_number = number
    number = int(input())

print(count)
print(biggest_jump)
