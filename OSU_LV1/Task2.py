while True:
    s = input()
    try:
        value = float(s)
    except:
        print("Invalid input. Please enter a numeric value.")
        continue

    if not (0.0 <= value <= 1.0):
        print("Number must be between 0.0 and 1.0.")
        continue

    if value >= 0.9:
        print("A")
    elif value >= 0.8:
        print("B")
    elif value >= 0.7:
        print("C")
    elif value >= 0.6:
        print("D")
    else:
        print("F")
    break