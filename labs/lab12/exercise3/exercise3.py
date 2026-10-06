grade = float(input())

total_grade = 0
valid_count = 0
while grade != -1:
    if (grade < 0) or (grade > 100):
        grade = float(input())
        continue
    else:
        total_grade += grade
        valid_count += 1
    grade = float(input())

average = total_grade / valid_count

print(valid_count)
print(f"{average:.2f}")
