
#seach particular element in a Set using user input
set = {1, 2, 3, 4, 5, 1, 2, 3}
print("Set: ", set)


ele = int(input("Enter the element to search in the set: "))

if ele in set:
    print(f"{ele} is present in the set.")
else:
    print(f"{ele} is not present in the set.")
