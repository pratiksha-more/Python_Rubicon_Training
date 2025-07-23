
# Dictionary - A dictionary is a collection which is unordered, changeable, and indexed. No duplicate members.
# Dictionaries are written with curly brackets, and they have keys and values.  
# to update a dictionary, you can directly assign a new value to an existing key or add a new key-value pair.

student={
    "name": "Pratiksha",
    "rollno": 26,
    "Percentage": 9.6,


}

print(student)
print("Type of student: ", type(student))

print()

print("Name :",student["name"])
print("Rollname : ",student["rollno"])
print("Percentage : ",student["Percentage"])

print()

print("*******Only keys**********")
for key in student:
    print(key)

print()

print("*******Keys Values**********")
for key in student:
    print(key ," :",student[key])
print()
    
