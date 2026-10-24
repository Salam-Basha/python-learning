# ==========================================
# LESSON 18: SCOPE
# ==========================================

# Local variable: Created inside a function.
# Global variable: Created outside a function.
# Functions can read global variables.
# Local and global variables can share a name.
# global keyword: Allows reassignment of a global variable.


#Exercise 1 — Local scope
#Create a function show_age() that creates a variable age = 18 and prints it.

def show_age():
    age = 18 
    print(age)

show_age()


#Exercise 2 — Global scope
#Create a global variable college = "RGM". Write a function show_college() that prints it. Call the function.


college = "rgm"

def show_college():
    print(college)

show_college()


#Exercise 3 — Same variable name

#Create a global variable language = "Python".
#Inside a function called change_language(), create a local variable with the same name and assign it "Java".
#Print language inside the function, call the function, then print language outside it.

language = "python"

def change_language():
    language = "java"
    print(language)

change_language()
print(language)




#Challenge 🎯 — Update a global variable

#Create a global variable points = 0.
#Write a function add_points() that uses global to change points to 10.
#Call the function and print points.


points = 0

def add_points():
    global points
    points = 10

add_points()
print(points)



# COMMON MISTAKES
# 1. Accessing a local variable outside its function.
# 2. Thinking a local variable changes a global variable.
# 3. Misspelling variable names.
# 4. Forgetting global when reassigning a global variable.

# END OF LESSON 18
# NEXT: LESSON 19 — PROBLEM-SOLVING FUNDAMENTALS
