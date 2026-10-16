#Exercise 1 — Print Hello

for i in range(5):
    print("hello,python")


#Exercise 2 — Print numbers

for i in  range(1,11):
    print(i)

#Exercise 3 — Multiplication table

number = int(input("enter a number"))
for i in range(1,11):
    print(number,"x",i,"=",number*i)


#Exercise 4 — Sum of numbers

total = 0 
for i in range(1,11):
    total = total + i
    print(total)

#Challenge 🎯 — Countdown

number =int(input("enter a value "))
for i in range(number,0,-1):
    print(i)

print("go")