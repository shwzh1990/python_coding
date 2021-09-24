import random
symbol_list = ["+", '-' ,'*', '/']

def Generate_homework(n):
    home_work_list = []
    for i in range(1,n+1):
        first_num = random.randint(1,100)
        second = random.randint(1, 100)
        symbol = random.choice(symbol_list)
        each_cal = str(first_num) + " " + symbol + " " + str(second) + " " + "=" + '\n'
        home_work_list.append(each_cal)
    with open("math home work.txt",'w') as fd:
        fd.writelines(home_work_list)

Generate_homework(10000)
