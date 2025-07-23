str="I Love Python "

print(str*2)  
print(str[0])
print(str[2:6])
print(str[7:]) 

print("Length Of String : ",len(str))  # Last character
print("Capatlized String: ", str.capitalize()) 
print("Uppercase String: ", str.upper())
print("Lowercase String: ", str.lower())
print("casefold String: ", str.casefold())
print("Centered String: ", str.center(50, '*'))
print("Ends with 'Python': ", str.endswith("Python"))
print("Ends with 'I': ", str.endswith("I"))
print("Starts with 'Python': ", str.endswith("Python"))
print("Starts with 'I': ", str.startswith("I"))


str1="Pratiksha"
str2="Patiksha@123"
str3="12345"



print("isalnum: ", str1.isalnum())  
print("isdigit: ", str1.isdigit())  
print("isspace: ", str1.isspace()) 
print("isdecimal: ",str1.isdecimal()) 
print("Identifier: ", str1.isidentifier())

print()

# print("isalnum: ", str2.isalnum())  
# print("isdigit: ", str2.isdigit())  
# print("isspace: ", str2.isspace()) 
# print("isdecimal: ",str2.isdecimal()) 

# print()
# print("isalnum: ", str3.isalnum())  
# print("isdigit: ", str3.isdigit())  
# print("isspace: ", str3.isspace()) 
# print("isdecimal: ",str3.isdecimal()) 


str4="Python"
str5="Programming"

print("Is str4 a valid identifier? ", str4.isidentifier())
print("Is str5 a valid identifier? ", str5.isidentifier())


print("IsStrip : ")
print(str5.strip())  

print("Original String: ", str)
new_str = str.replace("Python", "Java")
print("Replaced String: ", new_str)

mysplit = str.split()
print("Split String: ", mysplit)

#casefold
#capitalize
#center
#endwith
#startswith

