''' for x in range(1,11):
    print(x)

i=1
while i<=10:
    print(i)
    i+=1

'''
# Table of Contents:
print("Table ")
num=int(input("Enter a number: "))  

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Factorial of a number

for i in range(1, num + 1):
    if i == 1:
        fact = 1
    else:
        fact = fact * i

print("Factorial of", num, "is", fact)

# find Factors

print("Factors of", num, "are: ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)


