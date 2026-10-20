# ==========================================
# LESSON 14: break & continue 
# ==========================================

# break:
# Immediately stops the entire loop.

# continue:
# Skips the current iteration and moves to the next one.


# SYNTAX:

# break:
# if condition:
#     break

# continue:
# if condition:
#     continue


# IMPORTANT:
# break = stop the loop.
# continue = skip this iteration.
# Both can be used in for and while loops.


# ==========================================
# EXERCISE 1 — STOP AT 7
# Print numbers from 1 to 10, but stop before 7.
# ==========================================

for i in range(1, 11):
    if i == 7:
        break
    print(i)


# ==========================================
# EXERCISE 2 — SKIP NUMBER 5
# Print numbers from 1 to 10, but skip 5.
# ==========================================

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# ==========================================
# EXERCISE 3 — PRINT ONLY EVEN NUMBERS
# Print even numbers from 1 to 20 using continue.
# ==========================================

for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)


# ==========================================
# EXERCISE 4 — PASSWORD ATTEMPTS
# Keep asking until the correct password is entered.
# ==========================================

correct_password = "python123"

while True:
    entered_password = input("Enter password: ")

    if entered_password == correct_password:
        print("Login successful!")
        break


# ==========================================
# CHALLENGE — SKIP MULTIPLES OF 3
# Print numbers from 1 to 20.
# Skip multiples of 3 and stop at 17.
# ==========================================

for i in range(1, 21):
    if i % 3 == 0:
        continue

    if i == 17:
        break

    print(i)


# ==========================================
# COMMON MISTAKES
# ==========================================

# 1. break stops the entire loop, not just one iteration.
# 2. continue skips only the current iteration.
# 3. range(1, 11) includes 1 to 10, not 11.
# 4. In a while loop, ensure the loop can eventually stop.
# 5. Condition order matters when using break and continue.
