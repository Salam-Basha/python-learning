# =========================================
# LESSON 15: FUNCTIONS
# =========================================

# A function is a reusable block of code that performs a task.

# SYNTAX:
# def function_name():
#     # Code to execute
#
# function_name()      # Function call


# IMPORTANT:
# def = defines a function.
# Calling a function executes its code.
# Indentation defines the function body.
# A function can be called multiple times.


# ==========================================
# EXAMPLE 1 — BASIC FUNCTION
# ==========================================

def say_hello():
    print("Hello, Python!")

say_hello()


# ==========================================
# EXAMPLE 2 — FUNCTION WITH A PARAMETER
# ==========================================

def greet(name):
    print("Hello", name)

greet("Salam")
greet("pramod")
greet("Pooja")


# ==========================================
# EXAMPLE 3 — FUNCTION WITH TWO PARAMETERS
# ==========================================

def add(a, b):
    print(a + b)

add(10, 20)

# ==========================================
# EXERCISE 1 — YOUR FIRST FUNCTION
# Print "Welcome to Python!" and call the function once.
# ==========================================

def welcome():
    print("Welcome to Python!")

welcome()


# ==========================================
# EXERCISE 2 — REPEAT A MESSAGE
# Print "Keep learning!" by calling the function three times.
# ==========================================

def study():
    print("Keep learning!")

study()
study()
study()

# ==========================================
# EXERCISE 3 — GREET A PERSON
# Greet three different people using one function.
# ==========================================

def greet_person(name):
    print("Hello", name)

greet_person("Salam")
greet_person("Pramod")
greet_person("Pooja")


# ==========================================
# EXERCISE 4 — ADD TWO NUMBERS
# Print the sum of two numbers.
# ==========================================

def add_numbers(a, b):
    print(a + b)

add_numbers(10, 20)
add_numbers(7, 8)


# =========================================
# CHALLENGE — MULTIPLICATION TABLE
# Print the multiplication table of a number from 1 to 10.
# =========================================

def multiplication_table(number):
    for i in range(1, 11):
        print(number, "*", i, "=", number * i)

multiplication_table(5)


# ==========================================
# COMMON MISTAKES
# ==========================================

# 1. Forgetting the colon after the function definition.
# 2. Forgetting to indent the function body.
# 3. Defining a function but never calling it.
# 4. Using the wrong function name when calling it.
# 5. Passing the wrong number of arguments.
# 6. Remember: print() displays a result; return comes later
#    in Lesson 17 and sends a value back to the caller.
