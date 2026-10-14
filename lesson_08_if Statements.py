#Exercise 1 — Age checker
age = int(input("enter your age :"))
if age >= 18:
    print("You are eligible")

#Exercise 2 — Pass or fail

marks = 65 
if marks >= 40:
    print("pass")

marks = 25
if marks >= 40:
    print("pass")

#Exercise 3 — Positive numbe

number = int(input("enter value :"))
if number > 0:
    print("positive number")

#Exercise 4 — Divisibility check

number = int(input("enter a value :"))
if number % 5 == 0:
    print("divisible by 5")

#Challenge — Exam eligibility

marks = int(input("enter your marks :"))
attendance = float(input("enter your attendance :"))
if marks >= 40 and attendance >= 75:
    print("eligible for exam")
 

