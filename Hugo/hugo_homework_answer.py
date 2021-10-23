def anwser_1():
    num_list = [i for i in range(1,1000)]

    '''
    num_list = [1,2,3 .... 999]
    num 1=> index 0
    num 2=> index 1


    '''



    '''
    index: 
    a = [1,2,3,4,5]
     0 1 2 3 4
    a[0] => 1
    a[1] => 2
    a[4] => 5

    b = [32,53,453,2,432,53,2]
     0  1  2   3  4   5 6
    '''


    num = input("please type the number")
    index = num_list.index(int(num))
    print(index)


    num = input("please type the number")
    print(int(num)-1)

def answer_2():
    b = []
    name = input("please type your name")
    a_str="Jack:100,Lisa:89,Jason:96,Tom:67,Dan:90"
    a_list = a_str.split(',')
    for data in a_list:
        data_list = data.split(':')
        '''
        1. add result of the data_list in a new list
        '''
        b.append(data_list)
        '''
        2. use for loop to compare the name in the list and input.
        '''
        for student_info in b:
            if student_info[0] == name:
                print(student_info[1])
                break
def answer_2_2():
    student={}
    name = input("please type your name")
    a_str="Jack:100,Lisa:89,Jason:96,Tom:67,Dan:90"
    a_list = a_str.split(',')
    for data in a_list:
        data_list = data.split(':')
        '''
        1. build a new dict
        '''
        student[data_list[0]] = data_list[1]
    print(student[name])

def answer_3():
    a = input("what number did you choose for divisor?")
    for i in range(1,1000):
        if i % int(a) == 0:
            print(i)
answer_3()
