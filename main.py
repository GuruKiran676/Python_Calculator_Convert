
# Python Calculator and Unit Converter

# Calculator Function
def calculator():
    print("\n--- Calculator ---")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input! Enter a valid number.")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Enter a valid number.")

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose operation (1-4): ")

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation!")


# Kilometers to Miles Conversion
def km_to_miles():
    while True:
        try:
            km = float(input("Enter distance in kilometers: "))
            if km < 0:
                print("Distance cannot be negative!")
                continue

            miles = km * 0.621371
            print("Distance in miles:", round(miles, 2))
            break
        except ValueError:
            print("Invalid input! Enter a number.")


# Celsius to Fahrenheit Conversion
def celsius_to_fahrenheit():
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))

            fahrenheit = (celsius * 9/5) + 32
            print("Temperature in Fahrenheit:", round(fahrenheit, 2))
            break
        except ValueError:
            print("Invalid input! Enter a number.")


# Main Menu
while True:
    print("\n===== PYTHON CALCULATOR & CONVERTER =====")
    print("1. Calculator")
    print("2. Kilometers to Miles")
    print("3. Celsius to Fahrenheit")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        calculator()
    elif choice == "2":
        km_to_miles()
    elif choice == "3":
        celsius_to_fahrenheit()
    elif choice == "4":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice! Please try again.")
