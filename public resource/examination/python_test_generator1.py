'''
This is the python test generator for child programming

1. python sum all of the element in the list
2. python get the maximum element in the list
3. split string to the list
4. give random amount of string and print out mapping value
5. give a random long list and print out first one mid one and last one
6. create file called "test1.txt", and write string format: "<name>:<your name>@<age>:<age value>@<gender>:<your gender>@<weight>:<weight value>" for example name:Jack@age:32@gender:male@weight:80
7. open the file test1.txt and change the weight from your weight  to 67
8. please read out the info in the test2.txt the content present below 
   "Hugo":{
        "gender":"male",
        "age": 11,
        "weight":60
        }
9.  could you do a code when you run your code if you input your name then print out hello <your name> else print "sorry i do not you"
10. could you please print out the same element in the following 2 list
'''
import time
import random
import json
import string


class student_examination:

    def __init__(self,name, gender, age, weight):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        
        self.header = "'''\n \
This is the test for {0} python ability. Test hour: 1 hour\n \
Author/Teacher: Jack Shi \n \
Date: {1} \n \
Student:{2}\n \
\n\
Note: \n\
    1. Student should do the test by him/herself\n\
    2. Student can browse the python syntax from website\n\
    3. Student MUST sumbit the answer when time is up\n \
    \'''\n\n\n\n".format(self.name, time.asctime(time.localtime()),self.name) 

def convert_list2str(LIST):
    LIST = [str(element) for element in LIST]
    return '[' + ','.join(LIST) + ']'
def question_1(student_exam):
    question_list = [(element) for element in range(random.randint(1,100),random.randint(200,1000))]
    answer = str(sum(question_list))
    question_list = [str(element) for element in range(random.randint(1,100),random.randint(200,1000))]
    question_list = '[' + ','.join(question_list) + ']'
    question = "1.sum all of the element int the list presenting below:"
    return question,question_list,answer

def question_2(student_exam):
    question = "2. get the maximum element in the list for instance in the list [1,2,3,4,5] 5 is the largest number in the list so the answer is 5\n"
<<<<<<< HEAD
    question_list = [random.randint(1,3244) for i in range(1,10000)]
=======
    question_list = [random.randint(1,1000) for i in range(1,10000)]
>>>>>>> 76c1a5da8493c280e325f334a9aff560e123bfac
    answer = str(max(question_list))
    question_list = [element for element in question_list]
    question_list = convert_list2str(question_list)
    return question,question_list,answer

def question_3(student_exam):
    question = "3. Fetch all of the even number in the following string and save them in the list please print them out\n"
    question_list = [(random.randint(1,1000)) for i in range(1,10000)]
    answer = [str(odd_number) for odd_number in question_list if odd_number % 2 == 1]
    question_list = [str(element) for element in question_list]
    question_3_str = '%'.join(question_list)
    answer = '[' + ','.join(answer) + ']'
    return question, question_3_str,answer

def generate_dict():
    key = random.choices(string.ascii_uppercase, k=10)
    val = [i for i in range(1,10)]
    return '{' +','.join(['\"{0}\":{1}'.format(element_key,element_val) for element_key,element_val in zip(key,val)]) + '}'

def question_4(student_exam):
    question_str = generate_dict()
    question = "\n4. here give a string: {0}\n".format(question_str)
    question = question + "please make a function if input a key and print out the value\n" + "for instance:" + " if the string is {'a':1,'b':2}, then you function should type 'a' print out 1 and type 'b' print 2\n"

    answer = "\nstring_dict = {0}\n\
def answer_3(key):\n\
    print(string_dict[key])\n\
    ".format(question_str)

    return question, '', answer

def question_5(student_exam):
    question = '5. give a random long list and print out first one mid one and last one\n for instance if the list is [1,2,3,4,5,6,7,8,9,10] then the first one is 1 mid one is 6 the last one is 10\n'
    random_list = [random.randint(1,1000) for i in range(0,1000)]
    answer = "first one:{0},mid one: {1}, last one:{2}".format(random_list[0],random_list[len(random_list)//2],random_list[len(random_list)-1])
    random_list = convert_list2str(random_list)
    return question,random_list,answer

def question_6(student_exam): 
    question = '6. create file called "test1.txt", and write string format: "<name>:<your name>@<age>:<age value>@<gender>:<your gender>@<weight>:<weight value>" for example name:Jack@age:32@gender:male@weight:80\n'
    answer =  "\nwith open('test1.text', 'w') as fd:\n\
    fd.write('name:{0}@age:{1}@gender:{2}@weight:{3}')\n\
    ".format(student_exam.name, student_exam.age, student_exam.gender, student_exam.weight)
    return question,'', answer
def question_7(student_exam):
    question = '7. open the file test1.txt and change the weight from your weight to 67'
    
    answer =  "\nwith open('test1.text', 'w') as fd:\n\
    fd.write('name:{0}@age:{1}@gender:{2}@weight:67')\n\
    ".format(student_exam.name,student_exam.age,student_exam.gender)
    return question,'',answer
def question_8(student_exam):
    question = "8.(1) please read out the content in the test2.txt\n \
 (2) change the weight from 60 to 65 and change age  to your real age\n \
<<<<<<< HEAD
 (3) change weight value to your own weight value\n \
 (4) save the new data back to the test2.text file\n"
=======
 (3) change weight value to your own weight value\n"
>>>>>>> 76c1a5da8493c280e325f334a9aff560e123bfac

  #  question_list = '"{0}":{ \
  #         "gender":"male",\
  #         "age": {1},\
  #          "weighteight":{2}\
  #         }'.format(student_exam.name,random.randint(1,20),random.randint(1,100))
  #  print(question_list)
    question_list = {"{0}".format(student_exam.name): {'gender':"{0}".format(student_exam.gender),'age':random.randint(1,20),'weight':random.randint(1,100)  }}
    question_list = json.dumps(question_list)


    answer = {"{0}".format(student_exam.name) : {'gender':"{0}".format(student_exam.gender),'age':student_exam.age,'weight':student_exam.weight } }
    answer = json.dumps(answer)
    with open("test2.txt",'w',encoding='utf-8') as fd:
        fd.write(question_list)
    return question,question_list,answer

def question_9(student_exam):
    question = '9.  could you do a code when you run your code if you input your name then print out hello <your name> else print "sorry i do not you"\n'
    anwser = "\nwhile 1:\n\
    name = input('please type your name '')\n\
    if name != {0}:\n\
        print('student_examorry i do not you')\n\
    else:\n\
        print('hello {0}')\n\
        ".format(student_exam.name, student_exam.name)
    return question, '' ,anwser
def question_10(student_exam):
    question = '10. could you please print out the same element in the following 2 list\n'
    list_1 = [random.randint(1,1000) for i in range(1,2000)]
    list_2 = [random.randint(1,1000) for i in range(1,2000)]
    answer = set(list_1) & set(list_2)
    answer = [str(element) for element in answer]
    list_1 = [str(element) for element in list_1]
    list_2 = [str(element) for element in list_2]
    
    answer = '[' + ','.join(answer) + ']' + '\n'
    list_1 = '[' + ','.join(list_1) + ']' + '\n'
    list_2 = '[' + ','.join(list_2) + ']' + '\n'
    return question, list_1 + list_2, answer


#find out the minimum number in the following list
def question_11(student_exam):
<<<<<<< HEAD
    question = '11. Find out the minum number in the following list\n'
=======
    question = '11. Findind out the minum number in the following list\n'
>>>>>>> 76c1a5da8493c280e325f334a9aff560e123bfac
    question_list = [random.randint(342,4343) for i in range(1,100)]
    question_list = [str(element) for element in question_list]
    question_list = convert_list2str(question_list)
    answer = str(min(question_list))
    return question, question_list, answer
#combine two list into one
def question_12(student_exam):
    question = '12. Could you please combine following two list together? For instance if the list is a = [1,2,3] and b = [4,5,6] you answer should be c = [1,2,3,4,5,6]\n'
    list_1 = [i for i in range(1,20)]
    list_2 = [i for i in range(21,25)]
    list_1.extend(list_2)
    answer = 'code : list_1.extend(list_2) and the answer shoudl be' + convert_list2str(list_1)
    list_1 = convert_list2str(list_1)
    list_2 = convert_list2str(list_2)
    return question, list_1 + list_2, answer


def question_13(student_exam):
<<<<<<< HEAD
    question = "13. please remove the first element for the list by following. for instance if the list is a = [1,2,3,4,5] after remove operation the list should be a = [2,3,4,5]\n"
=======
    question = "13. please remove the first element for the list by following. for instance if the list is a = [1,2,3,4,5]\n"
>>>>>>> 76c1a5da8493c280e325f334a9aff560e123bfac
    question_list = [random.randint(43,455) for i in range(1,20)]
    question_list.pop(0)
    answer = convert_list2str(question_list)
    question_list = convert_list2str(question_list)
    return question, question_list, answer

def question_14(student_exam):
    question = "14. Could you please append the element presenting below to the following list? for instance if the list is [1,2] and the element is 3 then the result should be [1,2,3]\n"
    question_list = [random.randint(1,4) for i in range(1,3)]
    element =  random.randint(1,20)
    answer = "The sample code is list_a.append(element)"
    question_list = "list_1 = " + convert_list2str(question_list)+'\n' + 'element = ' + str(element)+'\n'
    return question, question_list, answer

def question_15(student_exam):
<<<<<<< HEAD
    question = '15. is there any syntax error in the following statement?\n'
    question_list = 'a = [1,2,3;4]\n\
    del a \n\
=======
    question = '15. is there any syntax error in the following statement?'
    question_list = 'a = [1,2,3;4] \
    del a \
>>>>>>> 76c1a5da8493c280e325f334a9aff560e123bfac
    print(a)'
    answer = "wrong, pleaese note the simicolon"
    return question, question_list, answer

def question_16(student_exam):
<<<<<<< HEAD
    question = '16. is there any syntax error in the following statement?\n'
    question_list = 'if a == 1\n \
    print("hello")'
    answer = "syntax wrong there is no colon after if statement"
    return question, question_list, answer

def question_17(student_exam):
    element = {"int": "{0}".format(random.randint(1,20)), "list": "{0}".format([random.randint(1,2443) for i in range(1,10)]),"dict":"{0}".format({"name":"{0}".format(student_exam.name)}), "float": "1.0"}
    answer = random.choice(list(element))
    question_list = str(element[answer])
    question =  "17. what is the type of the thing below?\n"
    return question, question_list, answer

def question_18(student_exam):
    question = "18. Could you print out the average value of following list?\n"
    question_list = [random.randint(43,434) for i in range(1,random.randint(23,45))]
    answer = sum(question_list) / len(question_list)
    question_list = convert_list2str(question_list)
    answer = str(answer)
    return question, question_list, answer
def question_19(student_exam):
    question = "19. could you remove all of the duplicate value in the following list?\n"
    question_list = [random.randint(43,434) for i in range(1,random.randint(23,42))]
    answer = convert_list2str(list(set(question_list)))
    question_list = convert_list2str(question_list)
    return question, question_list, answer
def my_minus(list_1, list_2):
    return list_1 - list_2
def question_20(student_exam):
    question = "20. Could you please minus each element one by one in the following lists?\n"
    list_1 = [random.randint(43,5356) for i in range(1,343)]
    list_2 = [random.randint(43,5356) for i in range(1,343)]
    answer = map(my_minus,list_1, list_2)
    list_1 = convert_list2str(list_1)
    list_2 = convert_list2str(list_2)
    return question,list1 + '\n' + list_2, answer


    

    
Questions = [question_1, question_2, question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10, question_11,  question_12, question_13, question_14, question_15, question_16, question_17]

=======
    question = '16. is there any syntax error in the following statement?'
    question_list = 'if a == 1 \
    print("hellow")'
    answer = "syntax wrong there is no colon after if statement"
    return question, question_list, answer

#def question_17(student_exam):
#    element = {"int": "".format(random.randint(1,20)), "list": "{}".format([random(1,2443) for i in range(1,10)]), "dict":"{0}".format({"name":"".format(student_exam.name)}), "float": "1.0"}
#    answer = random.choice(list(element))
#    question_list = str(element[answer])
#    question =  "17. what is the type of the thing below?"
#    return question, question_list, answer


    
Questions = [question_1, question_2, question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10, question_11,  question_12, question_13, question_14, question_15, question_16 ]
>>>>>>> 76c1a5da8493c280e325f334a9aff560e123bfac


def generate_examination(student_exam):
    final_examine = ''
    final_answer = ''
    for q in Questions:
        question, question_list, answer = q(student_exam)
        final_examine = final_examine +  question + question_list + '\n\n'
        final_answer =   final_answer  +  question + question_list + "\nThe answer is:" + answer + '\n\n' 
    with open("Examination.txt",'w',encoding='utf-8') as fd:
        fd.write(student_exam.header + final_examine)
    with open("Answer.txt",'w',encoding='utf-8') as fd:
        fd.write(student_exam.header + final_answer)

if  __name__ == "__main__":
#    student_name = input("Please input your name: ")
#    student_age =  input("please input your age: ")
#    student_gender = input ("please input your gender: ")
#    student_weight =input ("please input your weight: ")
#    student_exam = student_examination(student_name, student_gender,student_age,student_weight) 
    student_exam = student_examination('Jack', 'male',10,80)
    generate_examination(student_exam)
    
