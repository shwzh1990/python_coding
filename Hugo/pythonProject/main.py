'''
This is the project for children programming
This project is made by Jack Shi
project description:
1. help info
2. list all student info
3. add student info
4. remove student info
5. modify student info
6. check student info

file format:
v1.0 using txt file with each student in ench line info is split by ,
for instance
ID:123456,Name:Jack,Gender:male,Chinese:100,Math:100,English:100,Gym:100
ID:123457,Name:Jackson,Gender:male,Chinese:99,Math:99,English:99,Gym:99


hello word
'''

import os
import time





help_info_msg = "Hi welcome to my student transcript management software.\n" \
            "you can type 1 ~ 6 to select each options\n" \
            "Auther: Jack Shi\n" \
            "Date: 22/08/2021\n"
def help_info():
    print(help_info_msg)
    input("press enter key to continue...")

'''
So here we do the dict 
'''

def list_all_student_info():
    with open("student_info.txt",'r') as fp:
        student_msg_list = fp.readlines()
        for student_msg in student_msg_list:
            elements = student_msg.split(',')
            for element in elements:
                print(element + '\n')
        Quit_Character = input("press q to quit from the screen: ")
        if Quit_Character == 'q':
            menu_run()




def add_student_info():
    ID_list_in_file = []
    os.system('cls')
    with open("student_info.txt",'r') as fp:
        student_msg_list = fp.readlines()
    for student_msg in student_msg_list:
        elements = student_msg.split(',')
        ID_list_in_file.append(elements[0].split(':')[1])    #so now the python get all of the ID number for the student file
    while 1:
        New_Student_ID_num = input("please type new student's ID number: ")
        if New_Student_ID_num == 'q':
            break
        if New_Student_ID_num in ID_list_in_file:
            print("The ID you type in is existed, pleaese press ENTER to try again.")
            input()
            add_student_info()
        else:
            ID_list_in_file.append(New_Student_ID_num)
            new_student_name = input("please type new student name: ")
            new_student_gender = input("please type new student gender: ")
            new_student_chinese = input("please type new student chinese score: ")
            new_student_math = input("please type new student math score: ")
            new_student_Gym = input("please type new student Gym score: ")
            new_student_msg_list = ["ID:"+ New_Student_ID_num, 'Name:'+new_student_name, "Gender:"+new_student_gender, 'Chinese:'+new_student_chinese, "Math:"+new_student_math,\
                                    "Gym:"+new_student_Gym]
            new_student_msg_str = ','.join(new_student_msg_list) + '\n'
            with open("student_info.txt",'a') as fp:
                fp.write(new_student_msg_str)
'''
def remove_student_info():
    with open("student_info.txt", 'r') as fd:
        student_info_list = fd.readlines()
    print(student_info_list)
    while 1:
        ID_number = input("please type the student id number you want to delete")
        if ID_number == 'q':
            with open("student_info.txt", 'w') as fd:
                fd.writelines(student_info_list)
            break;

        i = 0
        for student_info in student_info_list:
            if ID_number in student_info:
                delete_student_list = student_info.split(",")
                for info in delete_student_list:
                    print(info + '\n')
                answer = input("are you sure to remove the student info above?(Y/N):")

                if answer == 'Y' or answer == 'y':
                    student_info_list.remove(student_info)
                    i = 0
                break
            i = i + 1
        if i == len(student_info_list):
            input("No id found press any key to continue....")
'''

'''
1. check is there any student info in the file 
2. if has student info then need user to give student ID
3. check input id with student id 
4. if match, present remove student id, and ask do you want remove student ID
5. remove id from list
6. open file and write new list into the file.

homework:
1. finish the remove_student_info
2. fix the invalid id number bug.
'''
def remove_student_info():
    #if there is no student in the file then print out "there is not student info in our file."
    with open("student_info.txt", 'r') as f:
        student_list = f.readlines()
    if student_list == []:                         #if there is no student in our file.
        print("there is no student in our file")
        input("press any button to exit")
    else:                                          #students in our file.
        #how to remove student info in the list
        remove_ID = input("please input remove student ID:")
        for student_info in student_list:
            if remove_ID in student_info:
                #use string.split to split the string
                remove_student_info_list = student_info.split(',')
                #print(remove_student_info_list)
                #add '\n' for each string
                for element in remove_student_info_list:
                    print(element+'\n')
                answer = input("Do you want to remove the student info? y/n:")
                if answer == 'y':
                    student_list.remove(student_info)
        # write the new list back to the file.
        with open("student_info.txt", 'w') as fd:
            fd.writelines(student_list)

def modify_student_info():

    ID_list_in_file = []
    student_str = ''
    os.system('cls')
    with open("student_info.txt",'r') as fp:
        student_msg_list = fp.readlines()
    for student_msg in student_msg_list:
        elements = student_msg.split(',')
        ID_list_in_file.append(elements[0].split(':')[1])    #so now the python get all of the ID number for the student file
    while 1:
        Student_ID_num = input("please type modify student's ID number: ")
        if Student_ID_num == 'q':
            break
        if Student_ID_num not in ID_list_in_file:
            input("The ID you type in does not existed, pleaese press ENTER to try again.")
        else:
            for element in student_msg_list:
                print(element)
                print(Student_ID_num)
                if Student_ID_num in element:
                    student_msg_list.remove(element)
                    student_name = input("Enter student name:")
                    student_gender = input("Enter student gender:")
                    student_chinese_score = input("Input chinese score:")
                    student_math_score = input("Input math score:")
                    student_gym_score = input("Input gym score:")
                    modified_student = ["ID:"+ Student_ID_num, 'Name:'+student_name, "Gender:"+student_gender, 'Chinese:'+student_chinese_score, "Math:"+student_math_score,\
                                       "Gym:"+student_gym_score]
                    student_str = ','.join(modified_student) + '\n'
                    student_msg_list.append(student_str)
                    with open("student_info.txt",'w') as fp:
                        fp.writelines(student_msg_list)

def check_student_info():
    ID_list_in_file = []
    os.system('cls')
    with open("student_info.txt",'r') as fp:
        student_msg_list = fp.readlines()
        if student_msg_list == []:
            input("there is no student info in the file. press enter to continue..")
            return
    i = 0
    while 1:
        os.system('cls')
        if student_msg_list == []:
            input("there is no student info in the file. press enter to continue..")
            break
        student_ID = input("Please type the student ID you want to check:")
        if student_ID == 'q':
                break
        for element in student_msg_list:
            i = i + 1
            if student_ID in element:
                infos_list = element.split(',')
                for info in infos_list:
                    print(info+'\n')
        if i == len(student_msg_list):
            input("The ID is not exist please press Enter to continue..")
            time.sleep(0.5)
            break



menu_dict = {"1":['help info',help_info],\
             '2':['list all student info',list_all_student_info], \
             '3': ['add student info',add_student_info], \
             '4': ['remove student info',remove_student_info], \
             '5': ['modify student info',modify_student_info], \
             '6': ['check student info',check_student_info] }


def menu_run():
    while 1:
        os.system('cls')
        for k,v in menu_dict.items():
            print(k,'.',v[0])
        select_num =  input("Please select from our menu: ")
        if select_num.isdigit() == False or (int(select_num) > len(menu_dict.keys()) and int(select_num) < 1):
            print("Sorry, please select the number from 1 ~ {}".format(len(menu_dict.keys())))
            os.system("cls")
            menu_run()
        else:
            os.system('cls')             #clear screen
            menu_dict[select_num][1]()


menu_run()






