'''
when i got a num:

try to use the number to fully divided by 2
if the nubmer can be fully divided by 2
then num = number / 2
else:
   try factor add by 1 => 2 + 1 = 3
   try if number can be fully divided by 3
   if can be fully divided by three then 
   num = num / 3 

'''
'''
my_list = []
factor = 2
num = input("Enter a number")
num = int(num)   #convert str to integer
if num < 2:
    print("no prime factor")
else:
    while num > 1:
        if num % factor == 0:
            my_list.append(factor)
            num = num / factor
        else:
          factor = factor + 1
print(my_list)
'''
from unittest import result


listmy_str = '343my_limit43454my_limit45365my_limit45325423my_limit324351432my_limit5243523543my_limit653462564my_limit89'
my_list = listmy_str.split("my_limit")
print(my_list)

'''
dictionary:

1000
[i for i in range(1,1000)]

my_dict = {"Joshua": 89, "Lisa": 87,"Tom": 59}
my_dict["Tom"]


1. how to build a new dictionary
my_dict = {}
2. how to add one element inside the dictionary 
   key:value note key must be a string
my_dict["Tom"] = 59
3. how to del one of the element inside a dictionary
del my_dict[XXXX]
4. how to remove all element in the dictionary
del my_dict
5. how to iterate(loop or visit all of the element inside the dict)
for key,value in my_dict.items()
6. how to get the keys in the dictionary:
for key in my_dict.keys()
7. how to get the value in the dictionary?
for key in my_dict.values()
'''
def question3():
    my_dict = {"A":1,"J":2,"S":3,"N":4,"H":6,"F":7,"J":8,"X":9}
    key = input("Please input a key")
    print(my_dict[key])

def question4():
    name = input("Please input your name")
    if name == "Joshua":
       print("Hello Joshua")
    else:
        print("I do not know you")

def question5():
    result_list = []
    my_list = ['shwzh1990@gmail.abc', 'James&gmail.com','Joshua@gmail.com', 'Lisa1988@163.com']
    for element in my_list:
        if "@" in element and element.endswith(".com"):
            result_list.append(element)
    print(result_list)
'''
set is tool to remove all of the duplicate value in the list
set(list)
'''