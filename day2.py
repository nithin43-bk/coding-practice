import math

def calculator():
    print("=" * 40)
    print("       PYTHON ADVANCED CALCULATOR")
    print("=" * 40)

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (**)")
        print("6. Square Root (√)")
        print("7. Modulus (%)")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "8":
            print("Thank you for using calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice!")
            continue

        try:
            if choice == "6":
                a = float(input("Enter a number: "))

                if a < 0:
                    print("Cannot calculate square root of a negative number.")
                else:
                    print("Result:", math.sqrt(a))

            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    print("Result:", a + b)

                elif choice == "2":
                    print("Result:", a - b)

                elif choice == "3":
                    print("Result:", a * b)

                elif choice == "4":
                    if b == 0:
                        print("Cannot divide by zero!")
                    else:
                        print("Result:", a / b)

                elif choice == "5":
                    print("Result:", a ** b)

                elif choice == "7":
                    if b == 0:
                        print("Cannot use zero as divisor!")
                    else:
                        print("Result:", a % b)

        except ValueError:
            print("Please enter valid numbers!")

calculator()
#Testing automatic push
