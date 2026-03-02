def total_euro(hours,payment):
    return float(workHours) * float(paymentPerHour)

print("Enter your work hours:")
workHours = input()
print("\nEnter your hourly payment:")
paymentPerHour = input()
print("\nTotal:", total_euro(workHours, paymentPerHour))

