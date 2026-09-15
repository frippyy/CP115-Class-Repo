position = input()
overtime_hours = int(input())
is_weekend = input()

if position == "Manager":
    base_hourly_rate = 30
elif position == "Supervisor":
    base_hourly_rate = 20
elif position == "Staff":
    base_hourly_rate = 15
elif position == "Intern":
    base_hourly_rate = 8

if overtime_hours > 8:
    overtime_pay = (base_hourly_rate * 8 * 1.5) + (base_hourly_rate * (overtime_hours - 8) * 2)
else:
    overtime_pay = base_hourly_rate * overtime_hours * 1.5

if is_weekend == "yes":
    overtime_pay += overtime_hours * 5

print(overtime_pay)
