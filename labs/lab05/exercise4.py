item_name = input("Enter the name of the item: ")
item_price = float(input("Enter the price of the item: "))

quantity = 3
tax_rate = 0.06

subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print(subtotal)
print(tax_amount)
print(total_cost)