#==========================================
#Membership Operators (in, not in)
#==========================================


#Exercise 1 — Letter Checker

word = "PROGRAMMING"
print("P" in word)
print("Z" in word)
print("A" not in word)


#Exercise 2 — Fruit Checker

fruits = ["apple", "banana", "mango", "orange"]
print("mango" in fruits)
print("grapes" in fruits)


#Exercise 3 — User Input\

sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")

print(letter in sentence)


#🎯 Challenge — Username Checker

username = input("Enter your username: ")

print("Contains @:", "@" in username)
print("Contains space:", " " in username)
print("Does not contain 123:", "123" not in username)



