# LESSON 20: F-STRINGS

# f-strings insert variables using {}
# Syntax: f"Hello {name}"
# Expressions work inside {}: f"{a + b}"
# No need to use str() for numbers.


# EXAMPLES
name = "Salam"
age = 18

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"Next year, I will be {age + 1}.")



#Exercise 1 — Personal Introduction
#Create variables name, age, and city.
#Print a sentence using an f-string.

name = "salam"
age = 18
city = "xyz"

print(f"my name is {name} , i am {age} old and i live in {city} city")


#Exercise 2 — Simple Calculator
#Create variables a = 20 and b = 10.
#Print their sum, difference, and product using f-strings.

a = 20 
b = 10

print(f"sum of a,b : {a+b}")
print(f"difference of a,b : {a - b}")
print(f"product of a,b : {a * b}")


#Exercise 3 — User Input
#Ask the user for their name and favourite colour.
#Print both in one sentence using an f-string.

name = input("enter your name :")
colour = input("enter your fav colour :")

print(f"my name is {name} . my fav colour is {colour}")


#Challenge — Shopping Bill

item = "Notebook"
price = 50
quantity = 3
total = price * quantity

print(f"item :{item}")
print(f"price :{price}")
print(f"quantuty :{quantity}")
print(f"total :{total}")




# COMMON MISTAKE
# "Hello, {name}"   -> Prints {name} literally
# f"Hello, {name}"  -> Inserts the variable



