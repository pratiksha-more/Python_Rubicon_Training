#statement.py
# 1) Conditional Branching Statements
    # i) Decision Making Statements
        #    - if statement
        #    - if-else statement
        #    - if-elif-else statement
        #    - nested if statement
    # ii) Selection Statements
        #    - switch statement (not available in Python, but can be simulated using if-elif-else)

# 2) Looping Statements
    # i) Iteration Statements
        #    - for loop
        #    - while loop
        #    - do-while loop (not available in Python, but can be simulated using while)
    # ii) Jump Statements
        #    - break statement
        #    - continue statement
        #    - pass statement
# 3) unconditional Statements


# Conditional Branching Statements
# Decision Making Statements
#if statement

x=int(input("Enter number: "))

if x > 0:
    print("Positive")


# if-else statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# if-elif-else statement with user input
x=int(input("Enter First number: "))
y=int(input("Enter second number: "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("y is greater than x")
else:
    print("x is equal to y")

# if-elif-else statement
n=int(input("Enter First number: "))

if n > 60:
    print("First")
elif n > 50:
    print("Second")
elif n > 40:
    print("Third")
else:
    print("Fourth")

# nested if statement
n=5;
if n > 2:
    if n > 3:
        print("n is greater than 3")
    print("n is greater than 2")

#nested if-else statement

x = 25

if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is between 11 and 20")
else:
    print("x is 10 or less")
