#set Operations

set= {1, 2, 3, 4, 5, 1, 2, 3,"A", "B", 10.5, 10+5j} 

print("Set: ", set)

print("Type of set: ", type(set))  
print("Length of set: ", len(set))  

set.add(6)  
print("Set after adding 6: ", set)

set.add("Pratiksha")
print("Set after adding 'Pratiksha': ", set)

set.update([11])
print("Set Update adding 11: ", set)

set.remove(2) 

set.discard(3)  
print("Set after discarding 3: ", set)

set.clear()  
print("Set after clearing: ", set)


del set  
print("Set after deletion: ", set)  


set1={"Apple","Orange","Cheery"}
set2={"Grapes","Mango"}

set3=set1.union(set2)
print("Set 3 : ",set3)
