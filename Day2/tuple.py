#Tuple - A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Tuples are written with round brackets.
# to update a tuple, you need to convert it to a list, make changes, and then convert it back to a tuple.

tuple=(1, 2, 3, 4, 5)
print("Tuple: ", tuple)
print("Type of tuple: ", type(tuple))  

print(tuple[0])#<class 'tuple'>
print(tuple[1:3])  # Slicing a tuple
print(tuple[1:])   # Slicing a tuple


for item in tuple:
    print("Item: ", item, "Type: ", type(item))
print()

# Tuple operations
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("A", "B", "C")
tuple3 = (10.5, 10 + 5j)

# Concatenation
tuple4 = tuple1 + tuple2 + tuple3
print("Concatenated Tuple: ", tuple4)


# Repetition
tuple5 = tuple1 * 2
print("Repeated Tuple: ", tuple5)

# Membership
print("Is 3 in tuple1? ", 3 in tuple1)
print("Is 'A' in tuple2? ", "A" in tuple2)


print("Count", tuple1.count(2))  # Count occurrences of an element
  

#Remove
del tuple1
#print(tuple1)

