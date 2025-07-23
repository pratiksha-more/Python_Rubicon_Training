
list1 = [1, 2, 3, 4, 5, "Patiksha", 10.5, 10 + 5j]
print("List: ", list1)
print("Type of list: ", type(list1))  
print("Length of list: ", len(list1))

print()


#convert list to tuple

tuple1 = tuple(list1)
print("Tuple: ", tuple1)
print("Type of tuple: ", type(tuple1))

print("Length of tuple: ", len(tuple1))


print()

#convert tuple to List

list2 = list(tuple1)
print("List after converting from tuple: ", list2)
