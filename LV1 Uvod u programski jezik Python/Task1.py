def total_euro(x,y):
    return float(x) * float(y)

#print("Enter your work hours:")
#workHours = input()
#print("\nEnter your hourly payment:")
#paymentPerHour = input()
#print("\nTotal:", total_euro(workHours, paymentPerHour))

while True:
    try:
        workHours = float(input("Enter your work hours: "))
        break
    except:
        print("Invalid input, enter a numeric value.")

while True:
    try:
        paymentPerHour = float(input("\nEnter your hourly payment: "))
        break
    except:
        print("Invalid input, enter a numeric value.")

print("\nTotal:", total_euro(workHours, paymentPerHour))
