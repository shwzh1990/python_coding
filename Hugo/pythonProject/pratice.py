'''
1. how to declare a empty list
'''
Joshua_list = []
print(Joshua_list)

'''
2. declare an unempty list
'''
Joshua_list = [1,2,3,4, "hello world", 1.256, True]
print(Joshua_list)

'''
3. how to add element into the list
'''
a = "Jack"
Joshua_list.append(a)
print(Joshua_list)


'''
4. how to remove an element from the list
   Pop will pop out the element at index
'''
Joshua_list.pop()
Joshua_list.pop()
Joshua_list.pop(1)
Joshua_list.pop(3)
print(Joshua_list)

'''
5. the second method to remove an element
'''
a = [3,2,"hello",3,5,6]
a.remove("hello")
print(a)

'''
6. reserve
'''
a = [1,2,3,4,5]
a.reverse()
print(a)

'''
7. sorted
'''
a = [43,541,3,54,2,4654,31,54,414,3,34,5,314,5,42,345,5,3415,4,45]
b = sorted(a)
print(b)

'''
8. clear
'''
a = [43,541,3,54,2,4654,31,54,414,3,34,5,314,5,42,345,5,3415,4,45]
a.clear()
print(a)


'''
practice
1. remove all  the odd number(1,3,5,7....) inside the following list
'''
'''
b = []
a = [75,4325,54,25,454,53,5,42,43,642,35,4325,642,4,325,34,65,6,5,43,54,35,4,5,435,456,4,54,35,45,4]
for number in a:   #for each number in a list
    if number % 2 == 0:   #we keep even number
        b.append(number)
print(b)
'''
a = [75,4325,54,25,454,53,5,42,43,642,35,4325,642,4,325,34,65,6,5,43,54,35,4,5,435,456,4,54,35,45,4]
b = [number for number in a if number % 2 == 0]
print(b)

'''
please print out all of the number can be divided by 2 and 3 in the range from 1 ~ 1000
'''
for i in range(1, 1001):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

'''
please print out all of the number can be divided by 2 or 3 in the range from 1 ~ 100
'''
for i in range(1, 101):
    if i % 2 == 0 or i % 3 == 0:
        print(i)

'''
please print out all the number can be divided by 7 and 21 and 31 in the range from 1 ~ 123456
'''

'''
please find out all of the value that can be divide by 2 or divided by 5 or divided by 7 in the following list 
and then add all values to a new list
and remove the all the number that can be divide by 21 and 45 in the new list.
'''
a = [i for i in range(1,123456)]


'''
please find out all of the value that can be divide by 2 or divided by 5 or divided by 7 in the following list 
and then add all values to a new list
and remove the all the number that can be divide by 21 and 45 in the new list.
'''
a = [i for i in range(1,123456)]
b = []
for number in a:
    if number % 2 == 0 or number % 5 == 0 or number % 7 == 0:
        b.append(number)

#print(b)
for number in b:
    if number % 21 == 0 or number % 45 == 0:
        b.remove(number)

#print(b)


'''
indentation practice
'''
'''
for i in range(1,3):
    for j in range(1,2):
        print("i = {0}, j = {1}".format(i, j))
    print("lmn")
print("opq")


for i in range(1,4):
    print("Jack") # 3
    for j in range(1,5):
        print("i = {0}, j = {1}".format(i, j)) # 12
    print("hello") # 3
print("world") #4
'''

a = [1,2,3,4,5,6,7,8]
b = a
b[1] = 20
print(a)
print(b)

del a
print(b)

'''
question: 
indentation and index

could you please remove all the element in the even index in the following list?
and add all the rest of the number in the new list


hint: for instance the list is a =[1,2,3,4,5,6]

for i in range(0,6):
    if i % 2 != 0:   i is odd number
        new_list.append(a[i])
'''
a = [i for i in range(123,45678)]






