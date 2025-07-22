print("Pratiksha")
x=10;
y=10;
z=x+y

print(z)


#Logical and Relational Operators
print("Logical and Relational Operators")
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter third number: "))    

if x>y and x>z:
    print("x is the largest number")
if y>x and y>z:
    print("y is the largest number")

if z>x and z>y:
    print("z is the largest number")


print()

#Assignment Operation
print("Assignment Operation")
# x=int(input("Enter first number: "))
# y=int(input("Enter second number: "))

x=10
y=20

print("Before addition, x is: ", x)
print("Before addition, y is: ", y)
x+=y
print()
print("After addition, x is: ", x)
print("After addition, y is: ", y)



print()
print("Before Sub, x is: ", x)
print("Before Sub, y is: ", y)
x-=y
print()
print("After Sub, x is: ", x)
print("After Sub, y is: ", y)

print()
print("Before Mul, x is: ", x)
print("Before Mul, y is: ", y)
x*=y
print()
print("After Mul, x is: ", x)
print("After Mul, y is: ", y)

print()
print("Before Div, x is: ", x)
print("Before Div, y is: ", y)
x%=y
print()
print("After Div, x is: ", x)
print("After Div, y is: ", y)


print()
#Bitwise Operators
print("Bitwise Operators")
x=6
y=3

print("x & y = ", x & y)
print("x | y = ", x | y)
print("x ^ y = ", x ^ y)
print("~x = ", ~x)
print("x << 2 = ", x << 2)  
print("x >> 2 = ", x >> 2)
print("y << 2 = ", y << 2)  
print("y >> 2 = ", y >> 2)
print()

#memberShip Operators
print("Membership Operators")
list1 = ["Pooja", "Pratiksha", "Sanjana","Gayatri"]

print("Pooja" in list1)  # True
print("Sanjana" not in list1)  # False
print("Riya" in list1)  # False
print("Gayatri" not in list1)  # False
print()


#Identity Operators
print("Identity Operators")
x=10
y=11
z=11
print(x is y)  # False
print(y is z)  # True
print(x is not y)  # True
print(y is not z)  # False

