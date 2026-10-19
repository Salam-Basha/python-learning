# ==========================================
# LESSON 13: range() — QUICK CHEAT SHEET
# ==========================================

# SYNTAX:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# IMPORTANT:
# The stop value is excluded.
# range(5) generates: 0, 1, 2, 3, 4


#Exercise 1 — Numbers from 1 to 10
#Use range() to print the numbers from 1 through 10.

for i in range(1,11):
    print(i)


#Exercise 2 — Even numbers
#Print all even numbers from 2 to 20 using range() and a step value.

for i in range(2,21,2):
    print(i)


#Exercise 3 — Multiples of 5
#Print the first 10 multiples of 5: 5, 10, 15, ... 50.

for i in range(5,51,5):
    print(i)


#Exercise 4 — Countdown
#Print numbers from 10 down to 1, then print "Go!".

for i in range(10,0,-1):
    print(i)
print("go!")


#Challenge 🎯 — Odd numbers backwards
#Print odd numbers from 19 down to 1 using range().

for i in range(19,0,-2):
    print(i)


# COMMON MISTAKES:
# range(1, 5) does NOT include 5.
# range(5) starts at 0.
# range() cannot have a step of 0.