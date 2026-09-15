day_type = input()
show_time = int(input())
customer_type = input()

if (customer_type == "Adult") and (day_type == "weekend"):
    base_price = 18
elif (customer_type == "Child") and (day_type == "weekend"):
    base_price = 12
elif (customer_type == "Senior") and (day_type == "weekend"):
    base_price = 15
elif (customer_type == "Adult") and (day_type == "weekday"):
    base_price = 15
elif (customer_type == "Child") and (day_type == "weekday"):
    base_price = 10
elif (customer_type == "Senior") and (day_type == "weekday"):
    base_price = 12

if show_time > 18:
    final_price = base_price + 3
else:
    final_price = base_price

print(base_price)
print(final_price)
