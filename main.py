
import random
import math

def calculator():
    print("\n--- Calculator ---")
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", "Cannot divide by zero" if b == 0 else a / b)
    else:
        print("Invalid operator")

def even_odd():
    n = int(input("Enter a number: "))
    print("Even" if n % 2 == 0 else "Odd")

def multiplication_table():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def factorial():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers")
    else:
        print("Factorial:", math.factorial(n))

def prime_checker():
    n = int(input("Enter a number: "))
    if n < 2:
        print("Not a prime number")
    elif all(n % i != 0 for i in range(2, math.isqrt(n) + 1)):
        print("Prime number")
    else:
        print("Not a prime number")

def guessing_game():
    secret = random.randint(1, 100)
    print("Guess a number between 1 and 100")

    while True:
        guess = int(input("Your guess: "))

        if guess == secret:
            print("Congratulations! Correct guess!")
            break
        elif guess < secret:
            print("Try a higher number")
        else:
            print("Try a lower number")

while True:
    print("\n===== PYTHON PROGRAM MENU =====")
    print("1. Calculator")
    print("2. Even or Odd")
    print("3. Multiplication Table")
    print("4. Factorial")
    print("5. Prime Number Checker")
    print("6. Number Guessing Game")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        calculator()
    elif choice == "2":
        even_odd()
    elif choice == "3":
        multiplication_table()
    elif choice == "4":
        factorial()
    elif choice == "5":
        prime_checker()
    elif choice == "6":
        guessing_game()
    elif choice == "7":
        print("Thank you for using Python!")
        break
    else:
        print("Invalid choice. Try again.")
# Testing automatic push