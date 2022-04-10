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
    question_list = [random.randint(1,1000) for i in range(1,10000)]
    answer = str(max(question_list))
    question_list = [str(element) for element in question_list]
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
    random_list = [str(random.randint(1,1000)) for i in range(0,1000)]
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
 (3) change weight value to your own weight value\n"

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

Questions = [question_1, question_2, question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10]


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
    student_name = input("Please input your name: ")
    student_age =  input("please input your age: ")
    student_gender = input ("please input your gender: ")
    student_weight =input ("please input your weight: ")
    student_exam = student_examination(student_name, student_gender,student_age,student_weight) 
    #student_exam = student_examination('Jack', 'male',10,80)
    generate_examination(student_exam)
    
