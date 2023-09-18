student_lunch_times = float(input("How many times a week do you eat at the student cafeteria?: "))
student_lunch_price = float(input("The price of a typical student lunch?: "))
weekly_grocery_expenditure = float(input("How much money do you spend on groceries in a week?: "))

daily_spendings = (student_lunch_times*student_lunch_times)/7 + weekly_grocery_expenditure/7
weekly_spendings = weekly_grocery_expenditure + student_lunch_price*student_lunch_times

print("Average food expenditure:")
print(f"Daily: {daily_spendings:10.2f}")
print(f"Weekly: {weekly_spendings:10.2f}")