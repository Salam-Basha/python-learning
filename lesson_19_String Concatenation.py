# LESSON 19: STRING CONCATENATION


# + joins strings: "Hello" + "World"
# Add spaces: "Hello" + " " + "World"
# Convert numbers: "Age: " + str(18)
# Repeat strings: "Hi " * 3
# input() returns a string.
# Never use + directly between a string and an integer.



#Exercise 1 — Full Name

first_name = "salam"
last_name = "basha"

full_name = first_name +" " + last_name

print("my full name ia",full_name)


#Exercise 2 — Personal Introduction

name = "Salam"
age = 18
city = "xyz"

print("my name is", name,". i am", int(age),"yrs old , i live in",city)


#Exercise 3 — Join User Input

fav_colour = input("enter your fav colour ")
fav_food = input("enter your fav food ")

print("my fav colour is",fav_colour,"and my fav food is",fav_food)


# Challenge — Simple Receipt

item = "Notebook"
price = 50
quantity = 3
total = price * quantity

print("item: ",str(item))
print("price: ",int(price))
print("quantity: ",int(quantity))
print("total: ",int(total))




# COMMON MISTAKES
# "Age: " + 18       -> TypeError
# "Age: " + str(18)  -> Correct
# "Hello" + "World"  -> HelloWorld (no space)
