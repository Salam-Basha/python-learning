#Exercise 1 — Pass or fail

marks = int(input("enter your marks :"))
if marks >= 40:
    print("pass")
else:
    print("fail")

#Exercise 2 — Voting eligibility

age = int(input("enter your age :"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#Exercise 3 — Positive or negative

number = int(input("enter a value :"))
if number >= 0:
    print("Positive or zero")
else:
    print("Negative")

#Exercise 4 — Even or odd

number = int(input("enter a value :"))
if number % 2 == 0:
    print("even")
else:
    print("odd")

#Challenge — Exam eligibility

marks = int(input("enter your marks :"))
attendence = float(input("enter your attendence:"))
if  marks >= 40 and attendence >=75:
    print("eligible for exam")
else:
    print("not eligible for exam")


