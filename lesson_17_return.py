# ==========================================
# LESSON 17: RETURN
# ==========================================

# return sends a value back to the caller.
#
# print() displays a value.
# return gives a value back to the code.
#
# return also stops the function immediately.




#Exercise 1 — Return a sum
#Create add(a, b) that returns the sum. Store the result in answer and print it.

def add(a,b):
    return a + b

answer = add(10,5)
print(answer)


#Exercise 2 — Square a number
#Create square(number) that returns the number multiplied by itself. Print the result of square(6).

def square(number):
    return (number * number)

product = square(6)
print(product)


#Exercise 3 — Use a returned value
#Create multiply(a, b) that returns the product. Store the result of multiply(4, 5) in a variable, then print that result plus 10.

def multiply(a,b):
    return(a * b)

product = multiply(4,5)
print(product)
print(product + 10)


#Challenge 🎯 — Pass the result to another function
#Write a function double(number) that returns twice the number.

def double(number):
    return(number * 2)

answer = double(8)
print(answer)



# ==========================================
# COMMON MISTAKES
# ==========================================

# 1. Defining a function but forgetting to call it.
# 2. Using print() when you need to return a value.
# 3. Forgetting that return stops the function.
# 4. Using / instead of % to check the remainder.
# 5. A function without return gives None by default.


