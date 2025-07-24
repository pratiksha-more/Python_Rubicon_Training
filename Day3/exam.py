li = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
print (li[1][-1])


li = [1, 2, 3, 4]
li.append([5,6,7,8])
print(li) 


def addToList(a):
    a += [10]

b = [10, 20, 30, 40]
addToList(b)
print (len(b)) 



def gfg(x,li=[]):
    for i in range(x):
        li.append(i*i)
    print(li)

gfg(3,[3,2,1]) 

# statement 1
li = range(100, 110)

# statement 2
print (li.index(105))


a = [1, 2, 3, 4, 5]
b = a
b[0] = 0;

print(a)  


a = ['physics', 'chemistry', 1997, 2000] 
print (a[1][-1])


a = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for', 'Geeks']]
print(len(a))


a = [10, 20, 30, 40, 50] 
b = [1, 2, 3, 4, 5] 
subtracted = list() 

for a, b in zip(a, b): 
    item = a -b 
    subtracted.append(item) 
print(subtracted)


a = ['Learn', 'Quiz', 'Practice', 'Contribute']
b = a
c = a[:]

b[0] = 'Code'
c[1] = 'Mcq'

count = 0
for c in (a, b, c):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'Mcq':
        count += 10

print (count) 