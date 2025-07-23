
print("******** List********")

#1. find The minimum value in a list

list1=[1,2,67,34,78,0]

# minimum=list1[0]
# for i in list1:
#     if i < minimum:
#         minimum = i

# print("Minimum value in the list is: ", minimum)
print("Minimum value in the list is: ", min(list1))


#2. find The minimum value in a list

list1=[1,2,67,34,78,0]

# maximum=list1[0]
# for i in list1:
#     if i > maximum:
#         maximum = i

# print("Maximum value in the list is: ", maximum)

print("Maximum value in the list is: ", max(list1))


print()
print("********Set********")


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 3 write commman element in two set
common_elements = set1.intersection(set2)
print("Common elements in set1 and set2: ", common_elements)

#4 write unique element in two set
unique_elements=set1.union(set2)
print("Unique elements in set1 and set2: ",unique_elements)

print()
print("********Tuple********")
tuple1=(1,3,78,14,78)
# 4. find the maximum value in a tuple
print("Maximum Value in tuple",max(tuple1))


print()
print("********Dictionary********")

#5. merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1,**dict2}


print("Merged Dictionary: ", merged_dict)

#6. Maximum value in a dictionary
dict3 = {'a': 1, 'b': 2, 'c': 3}
max_value = max(dict3.values()) 
print("Maximum value in the dictionary: ", max_value)


