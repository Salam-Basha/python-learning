#Exercise 1 — Grade calculator

marks = int(input("enter your marks :"))
if marks >= 90:
    print("excellent")
elif marks >= 75:
    print("very good")
elif marks >= 50:
    print("pass")
else:
    print("fail")

#Exercise 2 — Positive, negative, or zero

number = int(input("enter a value"))

if number > 0 :
    print("positive")
elif number < 0:
    print("negative")
elif number == 0:
    print("zero")

#Exercise 3 — Age category

age = int(input("enter your age :"))

if age < 13:
    print("child")
elif age < 19:
    print("Teenager")
elif age < 59:
    print("adult")
else:
    print("senior")


# Exercise 4 — Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")


# Challenge — Electricity Consumption

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    print("Low consumption")
elif units <= 300:
    print("Medium consumption")
else:
    print("High consumption")





