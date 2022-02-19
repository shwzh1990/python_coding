'''

sum 1 to 2000
'''
'''
f=1
u=1
for i in range(1999):
    u=u+1
    f=f+u
print(f)


a = [23,45,6,7,8,5,4,67,5,755,7544,64,35,68,9,64,5,23,43,2,0]

u=a[0]

for i in a:
    if u>i:
        u = i

print (u)
'''
'''
a=input("please write first number")
b=input("please write second number")
h=int(a)+int(b)
print(h)

'''
'''
f=1

for i in range(1,101):

    f=f*i
print(f)
'''

'''
please print out all the value (from range 1~7000) can be divided by 5


mode:
x % y == 0  means x can be divided by y


mode:
x % y == 0  means x can be divided by y
'''







'''
a=input("what number did you choose for divisor?")
for u in range(7000):
    if int(u) % int(a)== 0:
        print(u)

'''

'''
for i in range(1234,5678):
    if (i) % (2)==1:
        print(i)

a=1
b=1
c=0
for i in range(3,100):
    c=a+b
    a=b
    b=c
print(c)
'''
'''
a = [32,54,34,32,43,13,5143,-9,1,3,3,13,41,3,41,3,4,1,43,43,4,3,1,43,4,3,31,4,34,3,43,3,4,3,453,5,4,3,4,3,423,43,43,-7,5,1,3,14,3,43,5,345,3,4,13,432,53,4,3,4,3,43,5,9]
e=a[0]
f=a[e+1]
c=0
for i in a:
    c=e+f
    e=f
    f=c
f=c % 64
print(f)

print(sum(a)/len(a))
'''
'''
sum=0
def add (sum,a,b):
    for i in range(a,b):
        sum=sum+i
    return sum
c=add(sum,1,2001)
print(c)
'''
'''
def add(a,b):
    return a+b
def minus(c,d):
    return c-d
def multiply(e,f):
    return e*f
def devide(g,h):
    return g/h
'''
'''
def swap(a,b):

    c = a
    print("c = {0}".format(c))
    a = b
    print("a = {0}".format(a))
    b = c
    print("b = {0}".format(b))

f = 1
e = 2

swap(f,e)
print("f = {0}".format(f))
print("e = {0}".format(e))

b=[34,6,4312,43,14,3,43,21,432,14,3243454,325,4543,5,4325,34,5643,6,46,454,356,2345,46,4,23454,6,54]

u=b[0]
for i in b:
    if u > i:
        u=i
print(u)

u=b[0]
for i in b:
    if u < i:
        u=i
print(u)

b.sort()
print(b[0],b[-1])






b=[34,6,4312,43,14,3,43,21,432,14,3243454,325,4543,5,4325,34,5643,6,46,454,356,2345,46,4,23454,6,54]


b.pop (len(b)-1)

print(b)
'''
'''
a=input("please type the first number" )
b=input("please type the second number")
if a.isdecimal()==True and b.isdecimal()==True:
    c=int(a)+int(b)
    print(c)
else:
    print("this data is wrong,please try again")
'''
'''
done:
jack 18 male student
'''
'''
new_list = []
Text = "Name:Jack,Age:18,Gender:male,occupation:student"
new_text_list = Text.split(",")
for element in new_text_list:
    element_list = element.split(":")
    #print(element_list)
    new_list.append(element_list[1])
print (new_list)
'''
'''
def ryan(homework):
    result=0
    a=homework.splitlines()
    for i in a:
        b=i.split()
        if(b[1] == '+'):
            result = int(b[0]) + int(b[2])
        if (b[1] == '-'):
            result = int(b[0]) - int(b[2])
        if (b[1] == '*'):
            result = int(b[0]) * int(b[2])
        if (b[1] == '/'):
            result = int(b[0]) / int(b[2])
        b.append(str(result))
        print(b)
        finn=" ".join(b)
        print(finn)
    a=[]
    a="\n".join\
        (homework_result)
    print(a)
string_sample="1 + 1 =\n3456 * 343 =\n3242 / 2 =\n344 * 4315 ="
final=ryan(string_sample)
print(final)



homework = "1 + 1 = \n23 + 434 = \n24 / 6 = \n45 / 9 = \n12 * 4 = "

homework_result = "1 + 1 = 2\n23 + 434 = 457\n24 / 6 = 4\n45 / 9 = 5\n12 * 4 = 48"
ryan(homework)
print("1 + 1 = 2 23 + 434 = 457 24 / 6 = 4 45 / 9 = 5 12 * 4 = 48")
'''
'''
f = open("password.txt", 'r')
c = f.read()
f.close()



a=input("please type one username")
if a=="admin":
    c=input("please type a new password")
    f = open("password.txt", 'w')
    f.write(c)
    f.close()

b=input("please type one password")
if c==b:
    print("it's ok")

else:
    print("password is wrong")
'''

'''
'w' write data into the txt file, all the original data is wiped out before new data write in
    if the file is not exist, this w can build a new one.
    
'''
'''
f = open("password.txt",'w')
f.write("Huge")
f.close()

f = open("password.txt", 'r')
data = f.read()
print(data)
f.close()
'''

'''

string_sample="1 + 1 =\n3456 * 343 =\n3242 / 2 =\n344 * 4315 ="
final=ryan(string_sample)
print(final)



'''
'''
a = open("password.txt",'r')
raw_data = a.read()

a.close()
final_data = ryan(raw_data)
print(final_data)
'''
'''
a = open("password.txt",'w')
a.write
a.close()
'''
'''
def ryan(data):
    final_str = ""
    result = 0
'''
'''

sum = 0
for i in range(1,10001):
    sum=sum+i
print(sum)

#dictionary
'''
'''
sum = 0
for i in range(1,123456790):
    sum = sum + i
print(sum)
'''
#############################
'''
sum = 0

for i in range(1,65536):
    if i % 2 ==1:
        sum = sum + i
    elif i % 2 ==0:
        sum=sum-i
print(sum)


#############################
b=[32,4,31,1,4,31343,1,431,31,31,1,4,14,314,434,34,31,53,5,45,425,4,4,5,45,24,54,265,43,56,43654,634,5,435,435,43]

u=b[0]
for i in b:
    if u < i:
        u=i
print(u)
#############################
b=[32,4,31,1,4,31343,1,431,31,31,1,4,14,314,434,34,31,53,5,45,425,4,4,5,45,24,54,265,43,56,43654,634,5,435,435,43]

u=b[0]
for i in b:
    if u > i:
        u=i
print(u)
#############################
b=[]
a="Jack:100,Tom:89,Peter:64,Marry:34,Lisa:89,Tim:86,Tim:86,jackson:54,david:78"
a_list = a.split(',')
for data in a_list:
    data_list = data.split(':')
    b.append(data_list[1])
b.remove("100")
print(b)
c = ",".join(b)
print(c)

#############################
f = open("password.txt",'w')
f.write("Hugo")
f.close()

f = open("password.txt", 'r')
data = f.read()
print(data)
f.close()
'''
'''
import random


burger = 1
fish_and_chips = 2
pita_pit = 3
sandwich = 4
curry = 5
steak = 6

a = random.randint(1,6)
print (a)
if a == 1:
    print("burger")

if a == 2:
    print("fish_and_chips")

if a == 3:
    print("pita_pit")

if a == 4:
    print("sandwich")

if a == 5:
    print("curry")

if a == 6:
    print("steak")
'''
'''
'''
'''
menu_dict = {"1": "welcome to the student project,if you hit button 1,I will help you\nif you hit button 2,I will list student info\nif you hit button 3,I will add new student info\nif you hit button 4,I will  remove student info\nif you hit button 5,I will check student by ID\nif you hit button 6,I will modify student info.", "2": "list student info", "3": "add new student info", "4": "remove student info", \
             "5": "check student by ID", "6": "modify student info"}
def menu():
    for k, v in menu_dict.items():
        print(k, v)
    num = input("please select function: ")
    print(menu_dict[num])


while 1:
    menu()

  


f = open("test.txt", 'r')
data = f.read()
print(data)
f.close()
'''
# import random
#
# b=input("please type something to do(type number 1-6)")
# dict={1:"help info",2:"list student info",3:"add new student info",4:"remove student info",5:"check student by ID",6:"modify student info"}
# a=random.randint(1,len(dict))
# print(dict[a])

''''''
# import os
# help_info_smg = "hi, welcome to my student transcript management software.\n"\
#                 "you can type button 1-6 to select what to do.\n"\
#                 "Auther:Hugo Tan.\n"\
#                 "date:20/12/2021"

# #then,we goona open a nother file: student_info.txt
def unique_id(id):
    student_list=[]
    f = open("student_info.txt", 'r')
    student_info_list = f.readlines()
    for student_info in student_info_list:
        a=student_info.split(",")[0]
        b=a.split(":")
        student_list.append(b[1])
    if id in student_list:
        return True
    return False


'''
hello world
'''

#now,we goona print out all student that is in the file.
# def help_info():
#     os.system("cls")
#     print(help_info_msg)
#     input("press enter to back into the menu...")
#     menu()
# #in there, we needs to list all student info.
# def list_all_student_info():
#     f = open("student_info.txt", 'r')
#     student_info_list = f.readlines()
#     print(student_info_list)
#     for each_student_info in student_info_list:
#         elements = each_student_info.split(',')
#         print("-----------------------------------------------")
#         for element in elements:
#             print(element + '\n')
#     input()
#     f.close()
# def add_student_info():
#     os.system("cls")
#    #in there, we began to add student.
#     while 1:
#         new_student_id = input("please type new sudent ID:")
#         if unique_id(new_student_id) == True:
#             input("the student id exists please type again!")
#         else:
#     #In there, we needs to hands out some  questions about adding new students.
#             if new_student_id == 'q':
#                 break
#             new_student_name = input("please type new student name:")
#             new_student_gender = input("please type new student gender:")
#             new_student_chinese = input("please type new student chinese score:")
#             new_student_math = input("please type new student math score:")
#             new_student_gym = input("please type new student gym score:")
#             new_student_info = "ID:"     +new_student_id    + ','  +  \
#                                "Name:"   +new_student_name  + ','  +  \
#                                "Gender:"  +new_student_gender  + ','  +  \
#                                "Chinese:" +new_student_chinese   + ','  + \
#                                "Math:" +new_student_math  + ','  + \
#                                "gym:"  +new_student_gym+"\n"
#             with open ("student_info.txt",'a') as fd:
#                 #in there, we will adding the student that the user wants to typed.
#                     fd.write (new_student_info)

# #In there,if we don't have any student in our list, then we needs to reminds the user.
# def remove_student_info():
#      with open("student_info.txt",'r')as f:
#          student_list = f.readlines()
#      if student_list == []:
#          print("there is no student in our file.")
#          input("press any button to exit")
#      else:
#          #If we have at least one student in our list,we need to ask the user who and double check with the user in case the user desn't want to remove.
#          remove_ID = input("please input remove student ID:")
#          for student_info in student_list:
#              if remove_ID in student_info:
#                  remove_student_info_list = student_info.split(',')
#                  for element in remove_student_info_list:
#                      print(element+'\n')
#                  answer = input("Do you want to remove the student info?y/n:")
#                  if answer == 'y':
#                      student_list.remove(student_info)
#          with open ("student_info.txt",'w') as fd:
#         # in there, we will remove the student that the user wants to typed.
#             fd.writelines(student_list)
#
# #in there, we ask the student that the user wants to modify.
# def modify_student_info():
#     with open("student_info.txt", 'r') as f:
#         student_list = f.readlines()
#     a= input("which student did you want to modify?")
#     n=0
#     #now, we get the answer and ask user some questions.
#     for student_info in student_list:
#         if a in student_info:
#             ID_num = input("please type student ID:")
#             student_name = input("please input your name:")
#             student_gender = input("please input your gender:")
#             student_chinese_score = input("please input your chinese score:")
#             student_math_score = input("please input your math score:")
#             student_gym_score = input("please input your gym score:")
#             #at last, we modify the student to what the user wants to edit.
#             student_list[n] = "ID:" + ID_num + ',' + 'Name:' + student_name + ',' + 'Gender:' + student_gender + ',' + 'Chinese:' + student_chinese_score + ',' + 'Math:' +  student_math_score +','+'Gym:' + student_gym_score + '\n'
#     with open("student_info.txt",'w') as f:
#         f.writelines(student_list)
#
#
# #now,we will check the student that the user wants.
# def check_student_info():
#     check_ID = input("please input the student's ID that your want to check.")
#     with open("student_info.txt", 'r') as f:
#         student_list = f.readlines()
#     for student_info in student_list:
#         if check_ID in student_info:
#             print(student_info)
#         element_list=student_info.split(",")
#         for element in element_list :
#             print(element+"\n")
#
# #here is the buttons you needs to type if you wants to use the program.
# menu_dict = {"1":['help info',help_info],\
#              '2':['list all student info',list_all_student_info], \
#              '3': ['add student info',add_student_info], \
#              '4': ['remove student info',remove_student_info], \
#              '5': ['modify student info',modify_student_info], \
#              '6': ['check student info',check_student_info]}
#
# #Last, we will do the end.
# def menu():
#     while 1:
#         for k,v in menu_dict.items():
#             print(k + "."+ v[0])
#         num = input("please select number from 1 to {}".format (len(menu_dict)))
#         list_info = menu_dict[num]
#         list_info[1]()
#

#a=input("please type a number that you wants.")
#b=input("please type another number that you wants.")
#c=int(a)+int(b)
#print(c)
#number_list=[32,45,521,34,43,13,5,6,43,653,53,15,1,312,43,53,3]
#b=number_list[0]
#for i in number_list:
    #if b > i:
        #b = i
#print(b)
#number_list=[32,45,521,34,43,13,5,6,43,653,53,15,1,312,43,53,3]
#b=number_list[0]
#for i in number_list:
    #if b < i:
        #b = i
#print(b)
################################################################
#number_list=[32,45,521,34,43,13,5,6,43,653,53,15,1,312,43,53,3]
#number_list.append(31)
#print(number_list)
################################################################
#number_list=[45,521,34,43,13,5,6,43,653,53,15,1,312,43,53,3]
#number_list.pop()
#print(number_list)
################################################################
#number_list_2=[]
#number_list=[45,521,34,43,13,5,6,43,653,53,15,1,312,43,53,3]
#for number in number_list:
#    if number % 2 == 0:
#        number_list_2.append(number)
#print(number_list_2)
################################################################
#f = open("my_review.txt", 'r')
################################################################
#f = open("my_review.txt",'w')
#f.write("I am a student.")
#f.close()
#f = open("my_review.txt", 'r')
#data = f.read()
#print(data)
#f.close()


#questions:
#1.  who is the rank 1? (hard)
#2.  how many students? (easy): readline len(list)
#3.  how many female are there (easy)  split(":") judge index[1] == male /female
#4.  how many male(easy)      split(":") judge index[1] == male /female
#5.  list the student name who does has the highest score in chinese math gym English separately (medium)
#6.  what is the average score of each subject (medium)
#7.  how many students pass chinese, math, gym，English separately? (medium)
#8.  which students score is the lowest? (hard)
#9.  which student got the highest score in male (hard)
#10. which student got the highest score in female (hard)
#11. lowest score student for male (medium)
#12. lowest score for female (medium)

    #if highest_score < Total_score:
       # highest_score = Total_score
   # print(Total_score)
# b=[]
# a="Jack:100,Tom:89,Peter:64,Marry:34,Lisa:89,Tim:86,Tim:86,jackson:54,david:78"
# a_list = a.split(',')
# for data in a_list:
#     data_list = data.split(':')
#     b.append(data_list[0])
# b.remove("100")
# print(b)
# c = ",".join(b)
# print(c)
######################################################
# a = [23,45,6,7,8,5,4,67,5,755,7544,64,35,68,9,64,5,23,43,2,0]
#
# u=a[0]
#
# for i in a:
#     if u>i:
#         u = i

############################################
# #1. who are the rank 1?
# ###########################################
# f = open("student_info.txt")
# Total_score = 0
# C_score = 0
# M_score = 0
# E_score = 0
# G_score = 0
# highest_score = 0
# highest_score_name = []
# name= ""
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         a = element.split(":")
#         if a[0] == "Chinese":
#             C_score = int(a[1])
#         if a[0] == "Math":
#             M_score = int(a[1])
#         if a[0] == "English":
#             E_score = int(a[1])
#         if a[0] == "GYM":
#             G_score = int(a[1])
#     Total_score = C_score + M_score + E_score + G_score
#     if Total_score > highest_score:
#         highest_score = Total_score
#
#     for element in element_list:
#         a = element.split(":")
#         if a[0] == "Name":
#             name = a[1]
#         if Total_score == highest_score:
#             highest_score_name.append(name)
# highest_score_name.remove(highest_score_name[0])
# print("there are ",len(highest_score_name)," students  got the highest score.")
# print("these students have the highest score",highest_score_name,"their score is :",highest_score)
###############################################################
# #2. how many students?
# ##################################################################
# f = open ("student_info.txt", 'r')
# data = f.readlines()
# print(len(data))
# f.close()
# ####################################################################
# #3. how many females are there?
# ####################################################################
# f = open ("student_info.txt", 'r')
# female = 0
# male = 0
# data=f.readlines()
# for student_info in data:
#    element_list = student_info.split(",")
#    if element_list[2] =="gender:female":
#        female = female +1
#    else:
#        male = male+1
# print(female)
# f.close()
# ########################################################################
# #4. how many males are there?
# ####################################################################
# f = open ("student_info.txt", 'r')
# female = 0
# male = 0
# data=f.readlines()
# for student_info in data:
#    element_list = student_info.split(",")
#    if element_list[2] =="gender:female":
#        female = female +1
#    else:
#        male = male+1
# print(male)
# f.close()
# ####################################################################
#5.  list the student name who does has the highest score in chinese math gym English separately (medium)
####################################################################
# f = open("student_info.txt")
# ID = 0
# name = ""
# C_FHS = 0
# M_FHS = 0
# E_FHS = 0
# G_FHS = 0
# C_score = 0
# M_score = 0
# E_score = 0
# G_score = 0
# Chinese_highest_score = 0
# Math_highest_score = 0
# English_highest_score = 0
# Gym_highest_score = 0
# Chinese_highest_score_name = []
# Math_highest_score_name = []
# English_highest_score_name = []
# Gym_highest_score_name = []
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         g = element.split(":")
#         if g[0] == "Chinese":
#             C_score = int(g[1])
#         if g[0] == "Math":
#             M_score = int(g[1])
#         if g[0] == "English":
#             E_score = int(g[1])
#         if g[0] == "GYM":
#             G_score = int(g[1])
#         if C_score > Chinese_highest_score:
#             Chinese_highest_score = C_score
#         if M_score > Math_highest_score:
#             Math_highest_score = M_score
#         if E_score > English_highest_score:
#             English_highest_score = E_score
#         if G_score > Gym_highest_score:
#             Gym_highest_score = G_score
# C_FHS = Chinese_highest_score
# M_FHS = Math_highest_score
# E_FHS = English_highest_score
# G_FHS = Gym_highest_score
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         l = element.split(":")
#         if l[0] == "ID":
#             ID = int(l[1])
#         if l[0] == "Name":
#             name = l[1]
#         if l[0] == "Chinese":
#             C_score = int(l[1])
#         if l[0] == "Math":
#             M_score = int(l[1])
#         if l[0] == "English":
#             E_score = int(l[1])
#         if l[0] == "GYM":
#             G_score = int(l[1])
#     if C_score == C_FHS:
#         Chinese_highest_score_name.append(name)
#     if M_score == M_FHS:
#         Math_highest_score_name.append(name)
#     if E_score == E_FHS:
#         English_highest_score_name.append(name)
#     if G_score == G_FHS:
#         Gym_highest_score_name.append(name)
# print(len(Chinese_highest_score_name),"students have the highest score in Chinese:",Chinese_highest_score_name)
# print(len(Math_highest_score_name),"students have the highest score in Math:",Math_highest_score_name)
# print(len(English_highest_score_name),"students have the highest score in English:",English_highest_score_name)
# print(len(Gym_highest_score_name),"students have the highest score in Gym:",Gym_highest_score_name)
######################################################
#6.  what is the average score of each subject (medium)
#######################################################
# f = open("student_info.txt")
# Chinese_score = 0
# Math_score = 0
# English_score = 0
# Gym_score = 0
# Chinese_average_score = 0
# Math_average_score = 0
# English_average_score = 0
# Gym_average_score = 0
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         h = element.split(":")
#         if h[0] == "Chinese":
#             Chinese_score = Chinese_score+int(h[1])
#         if h[0] == "Math":
#             Math_score = Math_score+int(h[1])
#         if h[0] == "English":
#             English_score = English_score+int(h[1])
#         if h[0] == "GYM":
#             Gym_score = Gym_score+int(h[1])
#         Chinese_average_score = round(Chinese_score / len(data),2)
#         Math_average_score = round(Math_score / len(data), 2)
#         English_average_score = round(English_score / len(data), 2)
#         Gym_average_score = round(Math_score / len(data), 2)
# print("the chinese average score is",Chinese_average_score)
# print("the math average score is",Math_average_score)
# print("the english average score is",English_average_score)
# print("the gym average score is",Gym_average_score)
# f.close()
# ####################################################
# #7.  how many students pass chinese, math, gym，English separately? (medium)
# #########################################################################
# f = open("student_info.txt")
# Chinese_pass = 0
# Math_pass = 0
# English_pass = 0
# Gym_pass = 0
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         h = element.split(":")
#         if h[0] == "Chinese":
#             if int(h[1]) >= 60:
#                 Chinese_pass = Chinese_pass + 1
#         if h[0] == "Math":
#             if int(h[1]) >= 60:
#                 Math_pass = Math_pass + 1
#         if h[0] == "English":
#             if int(h[1]) >= 60:
#                 English_pass = English_pass + 1
#         if h[0] == "GYM":
#             if int(h[1]) >= 60:
#                 Gym_pass = Gym_pass + 1
# print(Chinese_pass,"students passed Chinese")
# print(Math_pass,"students passed Math")
# print(English_pass,"students passed English")
# print(Gym_pass,"students passed Gym")
##################################################################
#8.  which students score is the lowest? (hard)
###############################################
# f = open("student_info.txt")
# FLS = 0
# ID = 0
# name = ""
# Total_score = 0
# C_score = 0
# M_score = 0
# E_score = 0
# G_score = 0
# lowest_score = 500
# lowest_score_name = []
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         a = element.split(":")
#         if a[0] == "Chinese":
#             C_score = int(a[1])
#         if a[0] == "Math":
#             M_score = int(a[1])
#         if a[0] == "English":
#             E_score = int(a[1])
#         if a[0] == "GYM":
#             G_score = int(a[1])
#     Total_score = C_score + M_score + E_score + G_score
#     if Total_score < lowest_score:
#         lowest_score = Total_score
# FLS = lowest_score
# # print(FLS)
#
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         b = element.split(":")
#         if b[0] == "ID":
#             ID = int(b[1])
#         if b[0] == "Name":
#             name = b[1]
#         if b[0] == "Chinese":
#             C_score = int(b[1])
#         if b[0] == "Math":
#             M_score = int(b[1])
#         if b[0] == "English":
#             E_score = int(b[1])
#         if b[0] == "GYM":
#             G_score = int(b[1])
#     Total_score = C_score + M_score + E_score + G_score
#     if Total_score == FLS:
#         # print(ID,name,FLS)
#         lowest_score_name.append(name)
# print("this students have the lowest score",lowest_score_name,"his/her score is :",FLS)
# f.close()
#########################################################
#9.  which student got the highest score in male (hard)
#########################################################
# f = open("student_info.txt")
# FHS = 0
# ID = 0
# name = ""
# Total_score = 0
# C_score = 0
# M_score = 0
# E_score = 0
# G_score = 0
# highest_score = 0
# highest_score_name = []
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         v = element.split(":")
#         if v[0] == "Chinese":
#             C_score = int(v[1])
#         if v[0] == "Math":
#             M_score = int(v[1])
#         if v[0] == "English":
#             E_score = int(v[1])
#         if v[0] == "GYM":
#             G_score = int(v[1])
#
#     if element_list[2] == "gender:male":
#         Total_score = C_score + M_score + E_score + G_score
#         if Total_score > highest_score:
#             highest_score = Total_score
# FHS = highest_score
#
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         b = element.split(":")
#         if b[0] == "ID":
#             ID = int(b[1])
#         if b[0] == "Name":
#             name = b[1]
#         if b[0] == "Chinese":
#             C_score = int(b[1])
#         if b[0] == "Math":
#             M_score = int(b[1])
#         if b[0] == "English":
#             E_score = int(b[1])
#         if b[0] == "GYM":
#             G_score = int(b[1])
#     if element_list[2] == "gender:male":
#         Total_score = C_score + M_score + E_score + G_score
#         if Total_score == FHS:
#             highest_score_name.append(name)
# print("this students have the highest score in male:",highest_score_name,"his score is :",FHS)
# f.close()
# #########################################################
# #10. which student got the highest score in female (hard)
# #######################################################
# f = open("student_info.txt")
# FHS = 0
# ID = 0
# name = ""
# Total_score = 0
# C_score = 0
# M_score = 0
# E_score = 0
# G_score = 0
# highest_score = 0
# highest_score_name = []
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         a = element.split(":")
#         if a[0] == "ID":
#             ID = int(a[1])
#         if a[0] == "Chinese":
#             C_score = int(a[1])
#         if a[0] == "Math":
#             M_score = int(a[1])
#         if a[0] == "English":
#             E_score = int(a[1])
#         if a[0] == "GYM":
#             G_score = int(a[1])
#     if element_list[2] == "gender:female":
#         Total_score = C_score + M_score + E_score + G_score
#         if Total_score > highest_score:
#             highest_score = Total_score
# FHS = highest_score
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         b = element.split(":")
#         if b[0] == "ID":
#             ID = int(b[1])
#         if b[0] == "Name":
#             name = b[1]
#         if b[0] == "Chinese":
#             C_score = int(b[1])
#         if b[0] == "Math":
#             M_score = int(b[1])
#         if b[0] == "English":
#             E_score = int(b[1])
#         if b[0] == "GYM":
#             G_score = int(b[1])
#     if element_list[2] == "gender:female":
#         Total_score = C_score + M_score + E_score + G_score
#         if Total_score == FHS:
#             highest_score_name.append(name)
# print("this students have the highest score in female:",highest_score_name,"her score is :",FHS)
# f.close()
#########################################################
#11. lowest score student for male (medium)
#########################################################
# f = open("student_info.txt")
# FLS = 0
# ID = 0
# name = ""
# Total_score = 0
# C_score = 0
# M_score = 0
# E_score = 0
# G_score = 0
# lowest_score = 500
# lowest_score_name = []
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         a = element.split(":")
#         if a[0] == "Chinese":
#             C_score = int(a[1])
#         if a[0] == "Math":
#             M_score = int(a[1])
#         if a[0] == "English":
#             E_score = int(a[1])
#         if a[0] == "GYM":
#             G_score = int(a[1])
#
#     if element_list[2] == "gender:male":
#         Total_score = C_score + M_score + E_score + G_score
#         if Total_score < lowest_score:
#             lowest_score = Total_score
# FLS = lowest_score
#
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         b = element.split(":")
#         if b[0] == "ID":
#             ID = int(b[1])
#         if b[0] == "Name":
#             name = b[1]
#         if b[0] == "Chinese":
#             C_score = int(b[1])
#         if b[0] == "Math":
#             M_score = int(b[1])
#         if b[0] == "English":
#             E_score = int(b[1])
#         if b[0] == "GYM":
#             G_score = int(b[1])
#     if element_list[2] == "gender:male":
#         Total_score = C_score + M_score + E_score + G_score
#         if Total_score == FLS:
#             lowest_score_name.append(name)
# print("this students have the lowest score in male:",lowest_score_name,"his score is :",FLS)
# f.close()
#########################################################
#12. lowest score for female (medium)
#####################################################
# f = open("student_info.txt")
# FLS = 0
# ID = 0
# name = ""
# Total_score = 0
# C_score = 0
# M_score = 0
# E_score = 0
# G_score = 0
# lowest_score = 500
# lowest_score_name = []
# data = f.readlines()
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         a = element.split(":")
#         if a[0] == "ID":
#             ID = int(a[1])
#         if a[0] == "Chinese":
#             C_score = int(a[1])
#         if a[0] == "Math":
#             M_score = int(a[1])
#         if a[0] == "English":
#             E_score = int(a[1])
#         if a[0] == "GYM":
#             G_score = int(a[1])
#     if element_list[2] == "gender:female":
#         Total_score = C_score + M_score + E_score + G_score
#         if Total_score < lowest_score:
#             lowest_score = Total_score
# FLS = lowest_score
# for student_info in data:
#     element_list = student_info.split(",")
#     for element in element_list:
#         b = element.split(":")
#         if b[0] == "ID":
#             ID = int(b[1])
#         if b[0] == "Name":
#             name = b[1]
#         if b[0] == "Chinese":
#             C_score = int(b[1])
#         if b[0] == "Math":
#             M_score = int(b[1])
#         if b[0] == "English":
#             E_score = int(b[1])
#         if b[0] == "GYM":
#             G_score = int(b[1])
#     if element_list[2] == "gender:female":
#         Total_score = C_score + M_score + E_score + G_score
#         if Total_score == FLS:
#             lowest_score_name.append(name)
# print("this students have the lowest score in female:",lowest_score_name,"her score is :",FLS)
# f.close()
##################################################################
#system2
# f = open("math_homework.txt")
# result = 0
# result_list = []
# data = f.read()
# # print(data)
# a = data.splitlines()
# # print(a)
# for element in a:
#     b = element.split(" ")
#     # print(b)
#     if b[1] == "+":
#         result = int(b[0]) + int(b[2])
#         result_list.append(result)
#     if b[1] == "-":
#         result = int(b[0]) - int(b[2])
#         result_list.append(result)
#     if b[1] == "*":
#         result = int(b[0]) * int(b[2])
#         result_list.append(result)
#     if b[1] == "/":
#         result = round(int(b[0]) / int(b[2]),2)
#         result_list.append(result)
        # print(element,result)
# print(result_list)
########################################
# 1. Could you print out all of the odd number in the range 1 ~ 123435
# 2. get the result of sum = 1 + 2 + 3 + ....12345
# 3. now here is a string "Math score is 10" could you change the 10 to 60 and make the string like "Math score is 60"
# 4. could you establish a txt file called "note book.txt" and write some string into it?
# 5. design a function: you can type a password, then the code will compare your password with that in the txt file called password. if it is same then print out "welcome" else print please password is wrong please try again.
# you need to give user three times trail. if all trials are failed then exit from the code.
########################################################################################
#q1:could you print out all of the odd number in the range 1-123435(done)
# odd = 0
# even = 0
# odd_number_list = []
# for i in range(12345):
#     if int(i) % int(2) == 1:
#         odd_number_list.append(int(i))
# print(odd_number_list)
##################################################################
# #q2:get the result of sum = 1 + 2 + 3 + 4 + 5......+ 12345(done)
# sum = 0
# for i in range(12346):
#     sum = sum + i
# print(sum)
######################################################################
#q3:now here is a string "Math score is 10"could you change the 10 to 60 and make the string like"Math score is 60"?
# sentence = "Math score is 10"
# data = sentence.split(" ")
# data[3] = "60"
# print(data[0] + " " + data[1] + " " + data[2] + " " + data[3])
######################################################################################################
#q4:could you establish a txt file called "note book.txt" and write some string into it?(done)
###################################################################
# f = open("note_book.txt","w")
# f.write("234ghjl09")
# f.close()
#####################################################################################
#q5:design a function: you can type a password, then the code will compare your password with that in the txt file called password. if it is same then print out "welcome" else print please password is wrong please try again.you need to give user three times trail. if all trials are failed then exit from the code.(done)
# f = open("password.txt","w")
# f.write("12345")
# f.close()
# f.close()
# f = open("password.txt","r")
# j = f.read()
# a = input("please type a password")
# for i in range(3):
#     if a == j:
#         print("welcome")
#         break
#     else:
#         print("password is wrong, please try again.")
#         a = input("please type a password")
##################################################
# f = open("password.txt","w")
# f.write("0725hugo")
# f.close()
# f.close()
# f = open("password.txt","r")
# j = f.read()
# a = input("please type a password if you want to know a secret about hugo")
# for i in range(3):
#     if a == j:
#         print("go to hugo's room,then snooping under his bed, then you will get a paper.")
#         break
#     else:
#         print("password is wrong, please try again.")
#         a = input("please type a password")
##############################################################
#system3
import os
help_info_smg = "hi, welcome to my student transcript management software.\n"\
                "you can type button 1-6 to select what to do.\n"\
                "Auther:Hugo Tan.\n"\
                "date:20/12/2021"
#####################################################
# import random
# paper_mario_origami_king = 1
# mario_party = 2
# crazy_rabbit_party = 3
# Bowser_fury = 4
# Monopoly = 5
# mario_3d_world = 6
# # Hugo = 7
# # May = 8
# a = random.randint(1,6)
# if a == 1:
#     print("Today, we gonna play paper mario origami king.")
#
# if a == 2:
#     print("Today, we gonna play mario party.")
#
# if a == 3:
#     print("Today, we gonna play crazy rabbit party.")
#
# if a == 4:
#     print("Today, we gonna play Bowser's fury.")
#
# if a == 5:
#     print("Today, we gonna play monopoly.")
# if a ==6:
#     print("Today, we gonna play mario 3d world.")
####################################
# import random
# a = input("please type number 1-6")
# dict = {1:"help info",2:"list all student info",3:"add student info",4:"remove student info",5:"modify student info",6:"check student info"}
# b = random.randint(1,len(dict))
# print(dict[b])
##############################################
menu_dict = {"1":"welcome to my project, if you click button 1, I will help you. If you click button 2, I will list all student info. If you click button 3, I will add student info. If you click button 4, I will remove student info. If you click button 5, I will modify student info. If you click button 6, I will check student info.","2":"list all student info","3":"add student info","4":"remove student info","5":"modify student info","6":"check student info"}
def menu():
    for k, v in menu_dict.items():
        print(k, v)
    num = input("please select function: ")
    print(menu_dict[num])
# while 1:
#     menu()
# f = open("student_info.txt","r")
# data = f.read()
# print(data)
# f.close()

# def menu():
#     for k,v in menu_dict.items():
#         print(k,v)
#     num = input("please type a function:")
#     print(menu_dict[num])
# while 1:
#     menu()



# f = open("student_info.txt","r")
# data = f.read()
# print(data)
# f.close()

def unique_id(id):
    student_list = []
    f = open("student_info.txt","r")
    student_info_list = f.readlines()
    for student_info in student_info_list:
        a = student_info.split(",")[0]
        b = a.split(":")
        student_list.append(int(b[1]))
    # print(student_list)
    if id in student_list:
        # print("yes")
        return True
    else:
        # print("No")
        return False
#
# print(unique_id(249504667))
def help_info():
    os.system("cls")
    print(help_info_smg)
    print("please type enter to coutinue...")
    menu()
# help_info()
def list_all_student_info_list():
    f = open("student_info.txt","r")
    all_student_list = f.readlines()
    # print(all_student_list)
    for each_student_info in all_student_list:
        elements = each_student_info.split(",")
        print("----------------------------------------")
        for element in elements:
            print(element + "\n")
# list_all_student_info_list()
def add_student_info():
    os.system("cls")
    while 1:
        New_student_id = input("please type New student id")
        if New_student_id == "q":
            break
        else:
            if unique_id(int(New_student_id)) == True:
                input("the student id exists please type again!(click enter to continue...)")
            New_student_Name = input("please type the new Student's Name")
            if New_student_Name == "q":
                break
            New_student_gender = input("please type the new Student's Gender")
            if New_student_gender == "q":
                break
            New_student_chinese_score = input("please type the new student's Chinese Score")
            if New_student_chinese_score == "q":
                break
            New_student_math_score = input("please type the new student's Math Score")
            if New_student_math_score == "q":
                break
            New_student_english_score = input("please type the new student's English Score")
            if New_student_english_score == "q":
                break
            New_student_gym_score = input("please type the new student's GYM Score")
            if New_student_gym_score == "q":
                break
            New_student_info = "\n" + "ID:" + New_student_id + "," + \
                               "Name:" + New_student_Name + "," + \
                               "Gender:" + New_student_gender + "," + \
                               "Chinese:" + New_student_chinese_score + "," + \
                               "Math:" + New_student_math_score + "," + \
                               "English:" + New_student_english_score + "," + \
                                "GYM:" + New_student_gym_score
            with open("student_info.txt","a")as fd:
                fd.write(New_student_info)
# add_student_info()
##############################################
def remove_student_info():
    with open("student_info.txt","r") as f:
        student_list = f.readlines()
        if student_list == []:
            print("there is no student in our file.")
            input("please type enter to exist")
        else:
            Remove_ID = input("please type the remove student ID")
            if unique_id(int(Remove_ID)) == False:
                print("The input ID is not existed, please click the start button to run again.")
            for student_info in student_list:
                if Remove_ID in student_info:
                    Remove_student_info_list = student_info.split(",")
                    for element in Remove_student_info_list:
                        print(element + "\n")
                    answer = input("do you want to remove the student from the student list?(type y/n)")
                    if answer == 'y':
                        student_list.remove(student_info)
                    if answer == 'n':
                        break
            with open("student_info.txt","w") as fd:
                fd.writelines(student_list)
# remove_student_info()

def modify_student_info():
    with open("student_info.txt","r") as f:
        student_list = f.readlines()
        if student_list == []:
            print("there is no student in our file.")
            input("please type enter to exist")
        else:
            Remove_ID = input("please type the modify student ID")
            if unique_id(int(Remove_ID)) == False:
                print("The input ID is not existed, please click the start button to run again.")
            for student_info in student_list:
                if Remove_ID in student_info:
                    Remove_student_info_list = student_info.split(",")
                    for element in Remove_student_info_list:
                        print(element + "\n")
                    answer = input("are you sure that you want to modify the student from the student list?(type y/n)")
                    if answer == 'y':
                        student_list.remove(student_info)
                    if answer == 'n':
                        break
            with open("student_info.txt","w") as fd:
                fd.writelines(student_list)

        New_student_id = input("please type the modify student id")
        New_student_Name = input("please type the modify Student's Name")
        New_student_gender = input("please type the modify Student's Gender")
        New_student_chinese_score = input("please type the modify student's Chinese Score")
        New_student_math_score = input("please type the modify student's Math Score")
        New_student_english_score = input("please type the modify student's English Score")
        New_student_gym_score = input("please type the modify student's GYM Score")
        New_student_info = "\n" + "ID:" + New_student_id + "," + \
                           "Name:" + New_student_Name + "," + \
                           "Gender:" + New_student_gender + "," + \
                           "Chinese:" + New_student_chinese_score + "," + \
                           "Math:" + New_student_math_score + "," + \
                           "English:" + New_student_english_score + "," + \
                            "GYM:" + New_student_gym_score
        with open("student_info.txt","a")as fd:
            print("\n")
            fd.write(New_student_info)
# modify_student_info()
#     with open("student_info.txt","r") as f:
#         student_list = f.readlines()
#         if student_list == []:
#             print("there is no student in our file.")
#             input("please type enter to exist")
#         else:
#             Modify_ID = input("please type the modify student ID")
#             n = 0
#             if unique_id(int(Modify_ID)) == False:
#                 print("The input ID is not existed, please click the start button to run again.")
#             for student_info in student_list:
#                 element_list = student_info.split(",")
#                 a = element_list[0]
#                 b = a.split(":")
#                 c = b[1]
#                 if c == Modify_ID:
#                     h = element_list
#                     # print(h)
#                     # student_list.remove()
#                 new_ID = input("please type new ID")
#                 new_name = input("please type new Name")
#                 new_gender = input("please type new gender")
#                 new_chinese_score = input("please type new Chinese score")
#                 new_math_score = input("please type new Math score")
#                 new_english_score = input("please type new English score")
#                 new_gym_score = input("please type new Gym score")
#                 student_list[n] = "ID:" + new_ID + ',' + 'Name:' + new_name + ',' + 'Gender:' + new_gender + ',' + 'Chinese:' + new_chinese_score + ',' + 'Math:' +  new_math_score +','+'Gym:' + new_gym_score + '\n'
#             with open("student_info.txt","w")as f:
#                 f.writelines(student_list)
# modify_student_info()
#########################################################################################################################
# def modify_student_info():
#    with open("student_info.txt", 'r') as f:
#        student_list = f.readlines()
#    a= input("which student did you want to modify?")
#    n=0
#    for student_info in student_list:
#        if a in student_info:
#            ID_num = input("please type student ID:")
#            student_name = input("please input your name:")
#            student_gender = input("please input your gender:")
#            student_chinese_score = input("please input your chinese score:")
#            student_math_score = input("please input your math score:")
#            student_gym_score = input("please input your gym score:")
#            student_list[n] = "ID:" + ID_num + ',' + 'Name:' + student_name + ',' + 'Gender:' + student_gender + ',' + 'Chinese:' + student_chinese_score + ',' + 'Math:' +  student_math_score +','+'Gym:' + student_gym_score + '\n'
#    with open("student_info.txt",'w') as f:
#        f.writelines(student_list)
# modify_student_info()
def check_student_info():
    with open("student_info.txt","r") as f:
        student_list = f.readlines()
        if student_list == []:
            print("there is no student in our file.")
            input("please type enter to exist")
        else:
            Check_ID = input("please type the check student ID")
            if unique_id(int(Check_ID)) == False:
                print("The input ID is not existed, please click the start button to run again.")
            # for student_info in student_list:
            #     element_list = student_info.split(",")
            #     a = element_list[0]
            #     # print(a)#don't delete
            #     e = "ID:" + Check_ID
            #     if e == a:
            #         print(element_list)
            #     # print(e)#don't delete
            for student_info in student_list:
                a_list = student_info.split(",")
                b = a_list[0]
                # print(b)
                c = b.split(":")
                ID_number = c[1]
                # print(ID_number)
                if ID_number == Check_ID:
                    print(a_list)
# check_student_info()
# def menu_2():
#     while 1:
#         for k,v in menu_dict.items():
#             print(k + "."+ v[0])
#         num = input("please select number from 1 to {}".format (len(menu_dict)))
#         list_info = menu_dict[num]
#         print(list_info)
# menu_2()
#Disk, Ram, Keyboard, Mouse, Usb flash, Rom.
#the things I will learn in python at 2022:
#1.set(can learn at home)
#2.class(exception)
#3.json(can learn at home)
#4.tkinter
#5.project

#set
# set1 = {"hugo","May","Henry"}
# set2 = {"good","good","best"}
# print(set1)
# print(set2)

#json
# import json
# a = '{"Name":"Hugo","Age":"10","City":"China"}'
# b = json.loads(a)
# print(b["City"])
# x = {
# "Name" : "Hugo",
# "Age" : 10,
# "Gender" : "Male"
# }
# c = json.dumps(x)
# print(c)



# You can convert Python objects of the following types, into JSON strings:
#
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None


#When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null
# import json
# print(json.dumps({"Name" : "Hugo" , "Age" : 10}))
# print(json.dumps(99.123456789))
# print(json.dumps())
# import json
# x = {
#   "name": "Hugo",
#   "age": 10,
#   "pets": None
# }
# print(json.dumps(x))

# a = {1,2,3,2}
# b = {3,4,5}
# c = a & b
# print(c)

# a = {1,2,3,2}
# b = {3,4,5}
# c = a | b
# print(c)

# a = {1,2}
# b = {1,2}
# print(a == b)

# a = {1,2}
# b = {2}
# print(a - b)

# a = {1,2,3}s
# b = {3,4,5}
# print(a ^ b)

# a = [1,2,3]
# a[2] = 4
# print(a)

# a = [1,2,3,4]
# b = tuple(a)
# print(list(b))

# import json
# a = {"Hugo":{"programming lan":"c"}}
# result = json.dumps(a, indent=4)
# with open("0.txt","w")as fd:
#     fd.write(result)
# with open("0.txt","r")as fd:
#     info = fd.read()
# result = json.loads(info)
# print(result)
# class student:
#     def __init__(self,Name,School,Favourite_Subject):
#         self.Name = Name
#         self.School = School
#         self.Favourite_Subject = Favourite_Subject
# Hugo = student("Hugo","piegon mountain school","Math")
# print(Hugo.Name)
# print(Hugo.School)
# print(Hugo.Favourite_Subject)
class student:
    def __init__(self,Name,age,gender):
        self.Name = Name
        self.age = age
        self.gender = gender
    def prefer(self):
        if self.Name == "May":
            print("I prefer Drawing")
        if self.Name == "Hugo":
            print("I prefer Math")
May = student("May",7,"female")
Hugo = student("Hugo",10,"male")
May.prefer()