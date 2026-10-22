
# ============================================================
# LESSON 16 — PARAMETERS & ARGUMENTS
# ============================================================

# Parameter:
# A variable written inside the function definition.
# Example: name in def greet(name):

# Argument:
# The actual value passed when calling a function.
# Example: "Salam" in greet("Salam")

# One parameter:
# def greet(name):
#     print("Hello", name)

# Multiple parameters:
# def add(a, b):
#     print(a + b)
# add(10, 20)

# Positional arguments:
# Values are matched by their order.
# student_info("Salam", 18)

# Keyword arguments:
# Values are matched by parameter names.
# student_info(age=18, name="Salam")

# Default parameter:
# A parameter with a default value.
# def greet(name="Friend"):
#     print("Hello", name)

# If an argument is not provided, the default is used.

# IMPORTANT RULES

# 1. The number of required arguments must match
#    the number of required parameters.
# 2. Positional arguments are matched by order.
# 3. Keyword arguments are matched by name.
# 4. Default parameters can be left out when calling.
# 5. Parameters with defaults must come after
#    parameters without defaults.
# 6. Use ** for exponentiation: 2 ** 3 = 8.
# ============================================================


# ------------------------------------------------------------
# EXAMPLE 1 — ONE PARAMETER
# ------------------------------------------------------------

def greet_person(name):
    print("Hello", name)


greet_person("Salam")
greet_person("Pramod")


# ------------------------------------------------------------
# EXAMPLE 2 — TWO PARAMETERS
# ------------------------------------------------------------

def add_numbers(a, b):
    print(a + b)


add_numbers(10, 20)


# ------------------------------------------------------------
# EXAMPLE 3 — POSITIONAL ARGUMENTS
# ------------------------------------------------------------

def introduce(name, age):
    print(name, "is", age, "years old")


# Values are matched by order.
introduce("Salam", 18)


# ------------------------------------------------------------
# EXAMPLE 4 — KEYWORD ARGUMENTS
# ------------------------------------------------------------

def student_details(name, age):
    print(name, "is", age, "years old")


# Values are matched by parameter name.
student_details(age=18, name="Salam")


# ------------------------------------------------------------
# EXAMPLE 5 — DEFAULT PARAMETER
# ------------------------------------------------------------

def greet_with_default(name="Friend"):
    print("Hello", name)


# Uses the default value.
greet_with_default()

# Overrides the default value.
greet_with_default("Salam")


# ============================================================
# EXERCISES — WITH SOLUTIONS
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 — ONE PARAMETER
# Create greet(name) and call it with three names.
# ------------------------------------------------------------

def greet_exercise(name):
    print("Hello", name)


greet_exercise("Pramod")
greet_exercise("Pooja")
greet_exercise("Priya")


# ------------------------------------------------------------
# EXERCISE 2 — TWO PARAMETERS
# Create multiply(a, b) to print the product.
# ------------------------------------------------------------

def multiply(a, b):
    print(a * b)


multiply(4, 5)
multiply(7, 3)


# ------------------------------------------------------------
# EXERCISE 3 — STUDENT INFORMATION
# Call the function using positional and keyword arguments.
# ------------------------------------------------------------

def student_info(name, age):
    print(name, "is", age, "years old")


# Positional arguments
student_info("Salam", 18)

# Keyword arguments
student_info(age=18, name="Salam")


# ------------------------------------------------------------
# EXERCISE 4 — DEFAULT VALUE
# Call once without an argument and once with a name.
# ------------------------------------------------------------

def greet_default(name="Friend"):
    print("Hello", name)


greet_default()
greet_default("Salam")


# ============================================================
# CHALLENGE — SIMPLE CALCULATOR
# ============================================================

# Create a function that performs an operation
# based on the operation string.

def calculate(a, b, operation):

    if operation == "add":
        print(a + b)

    elif operation == "subtract":
        print(a - b)

    elif operation == "multiply":
        print(a * b)

    else:
        print("Invalid operation")


calculate(10, 5, "add")       # 15
calculate(10, 5, "subtract")  # 5
calculate(10, 5, "multiply")  # 50
calculate(10, 5, "divide")    # Invalid operation


# ============================================================
# MINI-TEST CHALLENGE — POWER FUNCTION
# ============================================================

# The exponent has a default value of 2.
# Use ** to calculate powers.

def power(base, exponent=2):
    print(base ** exponent)


power(5)      # 25 (default exponent is 2)
power(2, 3)   # 8


# ============================================================
# COMMON MISTAKES
# ============================================================

# MISTAKE 1: Missing a required argument
#
# def multiply(a, b):
#     print(a * b)

# multiply(5)  # TypeError: b is missing


# MISTAKE 2: Wrong keyword parameter name
#
# def greet(name):
#     print("Hello", name)
#
# greet(username="Salam")  # TypeError

# MISTAKE 3: Forgetting the function body
#
# def calculate(a, b):
#     # A function body is required.
#     pass

# MISTAKE 4: Placing a required parameter after a default
#
# def example(a=10, b):  # SyntaxError
#     print(a, b)
#
# Correct:
# def example(a, b=10):
#     print(a, b)

# MISTAKE 5: Confusing * and **
#
# 2 * 3   means multiplication → 6
# 2 ** 3  means exponentiation → 8


