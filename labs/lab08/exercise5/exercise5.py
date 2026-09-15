main_course = input()
drink = input()
dessert = input()

food_cost = 0

if main_course == "Chicken":
    food_cost += 10
elif main_course == "Beef":
    food_cost += 12
elif main_course == "Fish":
    food_cost += 11

if drink == "Soft Drink":
    food_cost += 2
elif drink == "Coffee":
    food_cost += 3

if dessert == "Ice Cream":
    food_cost += 4
elif dessert == "Cake":
    food_cost += 5

final_bill = food_cost * 1.10

print(f"{final_bill:.2f}")
