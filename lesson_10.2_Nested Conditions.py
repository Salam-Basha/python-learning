#Exercise 1 — Age and ID checker

age = int(input("enter your age : "))

if age >= 18:
    has_id = input("do you have your id (yes/no):")
    if has_id == "yes":
        print("entry allowed ")
    else:
        print("id required ")
else:
    print("underage ")

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













