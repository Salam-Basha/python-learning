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














