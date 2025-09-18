# Prompt the user for hours and rate
hours = input("Enter the hours: ")
rate = input("Enter the rate: ")

# Convert input strings to float
hours = float(hours)
rate = float(rate)

# Initialize pay
pay = 0.0

# Check if hours exceed 40
if hours > 40:
    # Hours above 40 are paid at 1.5 times the hourly rate
    # Calculate regular pay for first 40 hours
    regular_pay = 40 * rate
    # Calculate overtime pay for the remaining hours
    overtime_pay = (hours - 40) * rate * 1.5
    pay = regular_pay + overtime_pay
else:
    # If hours <= 40, then just regular pay
    pay = hours * rate

# Print the result
print(pay)
