#Exercise 1 — Print numbers

i = 1
while i <= 5:
    print(i)
    i = i + 1

#Exercise 2 — Countdown

i = 5
while i >= 1:
    print(i)
    i = i - 1
print("go")

#Exercise 3 — Sum of numbers

i = 1
total = 0

while i <= 10:
    total = total + i
    i = i + 1

print(total)


#Exercise 4 — Password checker

password = "python123"
entered_password = ""

while entered_password != password:
    entered_password = input("Enter your password: ")

print("Login successful")


#Challenge 🎯 — Number guessing game

number = 7
guessed_number = 0

while guessed_number != number:
    guessed_number = int(input("Guess the number: "))

print("Correct, you won!")



















