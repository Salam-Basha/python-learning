# Exercise 1 — Basic AND

a = 10
b = 20

print(a < b and b == 20)
print(a > b and b == 20)
print(a == 10 and b == 20)


# Exercise 2 — Basic OR

print(a > b or b == 20)
print(a > b or b < 10)
print(a == 10 or b == 10)


# Exercise 3 — Using NOT

is_student = True

print(not is_student)
print(not (10 > 5))
print(not (10 < 5))


# Exercise 4 — Age Eligibility

age = int(input("Enter your age: "))

print(age >= 18 and age <= 25)


# Challenge — Exam Eligibility

marks = int(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

print(marks >= 40 and attendance >= 75)
