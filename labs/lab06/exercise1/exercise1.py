# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

item1 = "Coffee"
item2 = "Muffin"
item3 = "Water"

price1 = 3.50
price2 = 2.10
price3 = 1.05

quantity1 = 2
quantity2 = 3
quantity3 = 4

tax_rate = 0.06

# Calculate totals
subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
tax = subtotal * tax_rate
total = subtotal + tax

# Print the receipt
print(f"========== RECEIPT ==========\nItem\t\tPrice\tQty\tTotal\n{item1}\t\t${price1:.2f}\t{quantity1}\t${price1 * quantity1:.2f}\n{item2}\t\t${price2:.2f}\t{quantity2}\t${price2 * quantity2:.2f}\n{item3}\t\t${price3:.2f}\t{quantity3}\t${price3 * quantity3:.2f}\n------------------------------\nSubtotal\t\t\t${subtotal:.2f}\nTax (6%)\t\t\t${tax:.2f}\nTotal\t\t\t${total:.2f}\n============================")