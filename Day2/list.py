list=[1,2,3,4,5,"Patiksha", 10.5, 10+5j ]
print(list)
print(type(list))  

for item in list:
    print(item,type(item))


# list.append(6)
# print("List after appending 6: ", list)


# list.remove(2)
# print("List after removing 2: ", list)

# list.insert(2, "NewItem")
# print("List after inserting 'NewItem' at index 2: ", list)

# list.pop()
# print("List after popping last item: ", list)

# list.reverse()
# print("List after reversing: ", list)


list1 = [90, 20, 30,50, 10 ,40, 90, 70, 80]
list2 = ["A", "B", "C"]
list3=[1, 2, 3.5, 4, 5.5]
list4 = [10,80, 30, 90, 50,'A', 'B', 'C', 'D', 10.5, 10+5j]
list1.sort()
list2.sort()
list3.sort()
list4.sort()
print("List1 after sorting: ", list1)
print("List2 after sorting: ", list2)
print("List3 after sorting: ", list3)
print("List4 after sorting: ", list4)