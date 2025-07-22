age=int(input("Enter your age: "))

if age < 18 and age >0:
    print(" You are a minor. Not eligible to vote.")
elif age >= 18:
    print("You are eligible to vote.")
else:
    print("Invalid age input.")

