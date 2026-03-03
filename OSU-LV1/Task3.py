lst = []

while True:
    x = input()
    if x == "Done":
        break

    try:
        number = float(x)
        
    except:
        print("Invalid input. Please enter a numeric value.")
        continue

    lst.append(number)

if not lst:
    print("No numbers were entered.")

print("Sorted list:", sorted(lst))
print("Count:", len(lst))
print("Average:", sum(lst) / len(lst))
print("Min/Max:", min(lst), max(lst))