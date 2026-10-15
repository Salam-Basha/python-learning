#Exercise 1 — Age and ID checker

age = int(input("enter your age : "))

if age >= 18:
    has_id = input("do you have your id (yes/no) :")
    if has_id == "yes":
        print("entry allowed")
    else:
        print("id required")
else:
    print("underage")


#Exercise 2 — Login checker

username = "salam"
password = "python123"
user = input("enter your name :")

if user == username:
    entered_password = input("enter yoour password:")
    if entered_password == password:
        print("login successfull")
    else:
        print("wrong password")
else:
    print("user name not found")

#Exercise 3 — Number checker

number = int(input("enter a value:"))

if number > 0:
    if number % 2 == 0:
        print("even number")
    else:
        print("odd number")
else:
    print("not a positive number")


# Challenge — Student result checker

marks = int(input("Enter your marks: "))

if marks >= 0 and marks <= 100:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid marks")












