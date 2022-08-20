def hello():
    print("Hello world")

def add(a,b):
    c = a + b
    print(c)

def print_gender(name:str, gender='male'):
    print(name, gender)

def add2(a,b):
    c = a + b
    return c
def straddstr(a:str,b:str) -> str:
    return a + b

def my_func(*kargs):
    return sum(kargs)

#if the student is a boy then
print_gender("Charles")
print_gender("Lisa","Female")

result = add2(1,2)

result = straddstr("Charles"," loves cat")
print(result)

result = my_func(1,2,3,4,5,6,7,8,9,10)
print(result)

'''
practice:
enter a parameter and return a sum result from 1 to this number and print it out
'''
def add3(a:int) -> int:
    my_list = [i for i in range(1,a)]
    result = sum(my_list)
    return result

result = add3(101)
print(result)

'''
practice, enter a parameter and return all number in range (a, 100000) can be divided by 2,3,4,5 in the same time.
'''

a = 1
b = 2

def swap(a,b):
    c = a
    a = b
    b = c

swap(a,b)

print(a)
print(b)
