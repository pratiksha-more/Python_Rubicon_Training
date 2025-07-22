a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
c=int(input("Enter Third number: "))

if a > b and a > c:
    print("a is the greatest")
elif b > a and b > c:
    print("b is the greatest")
elif c > a and c > b:
    print("c is the greatest")
else:
    print("All numbers are equal or no number is greater than the others")