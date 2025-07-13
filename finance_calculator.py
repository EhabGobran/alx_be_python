monthly_income = float(input("Enter your monthly income"))
monthly_expense = float(input("Enter your monthly expenses"))
rate = 0.05

monthly_savings = monthly_income - monthly_expense
yearly_savings = 12 * monthly_savings

projected_savings = yearly_savings + yearly_savings * rate

print("Enter your monthly income:", str(monthly_income))
print("Enter your total monthly expenses:", str(monthly_expense))
print("Your monthly savings are $"+str(monthly_savings))
print("Projected savings after one year, with interest, is: $"+ str(projected_savings))