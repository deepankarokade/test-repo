import op
print("Welcome to Q&A Calculator")

while True:
    print("\nChoose operation:")
    print("1 → Addition")
    print("2 → Subtraction")
    print("3 → Multiplication")
    print("4 → Division")
    print("5 → Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice not in ["1", "2", "3", "4"]
        print("Invalid choice. Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(Result:", num1 + num2

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", num1 / num2)
