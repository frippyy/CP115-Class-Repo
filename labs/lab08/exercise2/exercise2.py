employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

gross_salary = base_salary + (overtime_hours * 35)

if (tax_status == "Single") and (gross_salary >= 5000):
    tax_rate = 0.22
elif (tax_status == "Single") and (gross_salary < 5000):
    tax_rate = 0.18
elif (tax_status == "Married") and (gross_salary >= 6000):
    tax_rate = 0.20
elif (tax_status == "Married") and (gross_salary < 6000):
    tax_rate = 0.15
elif (tax_status == "Head") and (gross_salary >= 5500):
    tax_rate = 0.25
elif (tax_status == "Head") and (gross_salary < 5500):
    tax_rate = 0.19

deduction_tax_rate = gross_salary * tax_rate
deduction_epf = gross_salary * 0.11
deduction_socso = gross_salary * 0.005

net_salary = gross_salary - deduction_tax_rate - deduction_epf - deduction_socso

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
