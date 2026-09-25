percentage = float(input("Enter percentage: "))
income = int(input("Enter family income: "))

percentage_ok = percentage >= 75
income_ok = income <= 300000

print("Percentage ok:", percentage_ok)
print("Income ok:", income_ok)

if percentage_ok and income_ok:
    print("Scholarship eligible")
elif percentage_ok or income_ok:
    print("At least one condition is true")
else:
    print("Not eligible")
