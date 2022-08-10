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

practice7()

