monthly_income = int(input("Enter your monthly income? "))
monthly_expenses = int(input("Enter your total monthly expenses? "))

monthly_savings = monthly_income - monthly_expenses
interest = monthly_savings * 12 * 0.05

annual_savings = monthly_savings * 12 
projected_savings = annual_savings + (annual_savings * 0.05)

print(f"Your monthly savings are ${monthly_savings:}.")
print(f"Projected savings after one year, with interest, is {annual_savings:}")