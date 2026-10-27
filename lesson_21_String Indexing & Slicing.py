# LESSON 21: STRING INDEXING & SLICING

# word[0]     -> First character
# word[-1]    -> Last character
# word[1:4]   -> Index 1 to 3 (end excluded)
# word[:3]    -> First 3 characters
# word[2:]    -> Index 2 to end
# word[::2]   -> Every second character
# word[::-1]  -> Reverse string

#Exercise 1 — Character Finder

name = "PYTHON"

print(name[0])
print(name[-1])
print(name[2])


#Exercise 2 — Slicing Practice

word ="PROGRAMMING"

print(word[0:4])
print(word[3:8])
print(word[8:11])

#Exercise 3 — Reverse a String

name =input("enter your name")

print(name[::-1])


#Challenge — Name Analyzer

name =input("enter your name")

print(name[0])
print(name[-1])
print(name[::-1])
print(name[0:3])



# COMMON MISTAKES
# Indexing starts at 0.
# The ending index in a slice is excluded.
# An invalid index causes IndexError.
# Empty strings have no first or last character.
