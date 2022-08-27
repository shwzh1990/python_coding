def practice1():
    my_list = [1,1,1,2,2,2]
    my_list.append(2)
    print(my_list)
    my_list.pop(0)
    print(my_list)

def practice2():
    my_list = [1,1,1,2,2,2]
    my_list.remove(2)
    print(my_list)

def practice3():
    my_list = [1,2,3,4,5]
    print(len(my_list))

def practice4():
    my_dict = {"key1":{"key2":[1,2,3,5]}}
    print(my_dict["key1"]["key2"][0])

def practice5():
    my_list  = [1,1,2,3,4,3,4,2,4,10]
    my_set = set(my_list)
    print(my_set)

def practice6():
    my_list = [i for i in range(1,101)]
    print(my_list)

def practice7():
    my_list = [i for i in range(1,101) if i % 7 == 0]
    print(my_list)

def my_func():
    (A + B) * C + (D / G) * 3.14

'''
Function Example 1:
'''
def my_print():
    print("Hello World!")

'''
Function Example 2:
'''
def my_print2(name:str):
    print(name)

'''
Function Exmaple 3:
'''
def my_print3(name:str, age:int, Gender:str):
    print(name, age, Gender)

'''
Function Exmaple 4:
'''
def add(number1:int, number2:int):
    result = number1 + number2
    return result

#make a function with one parameter. The function will return the sum value from 1 to the specified parameter for instance if parameter is 100 the result shoule be
#1 + 2 + 3 .... 100 = 5050
#result = add2(100)
#print(result) => 5050
def add2(number:int) -> int:
    result = 0
    for i in range(1,number+1):
        result = result + i
    return result

my_result =  add2(100)

'''
Function Example 5:
'''
def system(name:str,age:int,language:str = 'English'):
    print(name, age, language)

system("Jack", 17, "English")

'''
Function Example 6:
'''
def add(*kargs):
    return sum(kargs)

print(add(1,2,3,4,5))
print(add(1,2,3))

'''
Function Example 6


a = 1
b = 2

c = a  => c  = 1
a = b  => a = 2 b = 2 c = 1
b = c  => a = 2 b = 1 c = 1
'''
#def swap(a,b):
#    c = a
#    print(a,b,c)
#    a = b
#    print(a,b,c)
#    b = c
#    print(a,b,c)
#    
#
#a = 1
#b = 2
#swap(a,b)
#print(a)
#print(b)
c = 10
def my_life():
    a = 1232

my_life()


'''
make a function the parameter is a list, the function can return a list with all element can be divide by 23

'''
def my_func(my_list:list) -> list:
    return [i for i in my_list if i % 23 == 0]

result = my_func([i for i in range(1,101)])

print(result)

'''
make a function with two paramter the first parameter is a list and the second parameter is a value, the function  should return the list which each element times with the 
second parameter:

for instance the first parameter is  [1,2,3,4,5] and the second is 2 then the result should be [2,4,5,8,10]
'''

#def my_function(my_list:list,num:int) -> list:
#    return_list = []
#    for i in my_list:
#        element = i * num 
#        return_list.append(element)
#    return return_list
#
def my_function(my_list:list,num:int) -> list:
    return [i * num for i in my_list]
result = my_function([1,2,3,4,5], 2)
print(result)  #=> [2,4,6,8,10]
