#=======================================
# LESSON 22: STRING METHODS
#=======================================
# .upper()      -> Uppercase
# .lower()      -> Lowercase
# .title()      -> Capitalize each word
# .capitalize() -> Capitalize first character
# .strip()      -> Remove spaces from both ends
# .replace(a,b) -> Replace text
# .find()       -> Find index (-1 if not found)
# .isalpha()    -> Check letters only
# .isdigit()    -> Check digits only
# .isalnum()    -> Check letters and digits
# .split()      -> Split into a list
# .join()       -> Join strings
# len()         -> Count characters

#=======================================
# EXAMPLE
text = "  hello python  "

print(text.upper())
print(text.strip())
print(text.replace("python", "world"))
#========================================

# EXERCISE 1: NAME FORMATTER
name = "  sALAM bASHA  "

print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())


# EXERCISE 2: REPLACE TEXT
sentence = "I am learning Java"
print(sentence.replace("Java", "Python"))


# EXERCISE 3: CHECK INPUT
value = input("Enter a value: ")

print("Digits only:", value.isdigit())
print("Letters only:", value.isalpha())


# CHALLENGE: USERNAME CHECKER
username = input("Enter a username: ")

print("Lowercase:", username.lower())
print("Letters and numbers only:", username.isalnum())
print("Length:", len(username))


# COMMON MISTAKES
# Methods need parentheses: text.upper()
# Strings are not changed in place by these methods.
# isdigit() and isalpha() return True or False.
# isalnum() returns False if the string contains spaces.

