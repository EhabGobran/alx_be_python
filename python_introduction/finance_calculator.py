monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expenses: "))


monthly_savings = monthly_income - monthly_expense
projected_savings = 12 * monthly_savings + (12 * monthly_savings * 0.05)

print("Your monthly savings are $"+str(int(monthly_savings)))
print("Projected savings after one year, with interest, is: $"+ str(int(projected_savings))+".")

