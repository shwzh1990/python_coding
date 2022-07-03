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
import numpy as np

Amount_of_question = 82,3,4,582,3,4,582,3,4,58
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
    question_list = convert_list2str(question_list)
    question = " sum all of the element int the list presenting below:"
    return question,question_list,answer

def question_2(student_exam):
    question = " get the maximum element in the list for instance in the list [1,2,3,4,5] 5 is the largest number in the list so the answer is 5\n"
    question_list = [random.randint(1,783) for i in range(1,10000)]
    answer = str(max(question_list))
    question_list = [element for element in question_list]
    question_list = convert_list2str(question_list)
    return question,question_list,answer

def question_3(student_exam):
    question = " Fetch all of the odd number in the following string and save them in the list please print them out\n"
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
    question = " here give a string: {0}\n".format(question_str)
    question = question + "please make a function if input a key and print out the value\n" + "for instance:" + " if the string is {'a':1,'b':2}, then you function should type 'a' print out 1 and type 'b' print 2\n"

    answer = "\nstring_dict = {0}\n\
def answer_3(key):\n\
    print(string_dict[key])\n\
    ".format(question_str)

    return question, '', answer

def question_5(student_exam):
    question = ' give a random long list and print out first one mid one and last one\n for instance if the list is [1,2,3,4,5,6,7,8,9,10] then the first one is 1 mid one is 6 the last one is 10\n'
    random_list = [random.randint(1,1000) for i in range(0,1000)]
    answer = "first one:{0},mid one: {1}, last one:{2}".format(random_list[0],random_list[len(random_list)//2],random_list[len(random_list)-1])
    random_list = convert_list2str(random_list)
    return question,random_list,answer

def question_6(student_exam): 
    question = ' create file called "test1.txt", and write string format: "<name>:<your name>@<age>:<age value>@<gender>:<your gender>@<weight>:<weight value>" for example name:Jack@age:32@gender:male@weight:80\n'
    answer =  "\nwith open('test1.text', 'w') as fd:\n\
    fd.write('name:{0}@age:{1}@gender:{2}@weight:{3}')\n\
    ".format(student_exam.name, student_exam.age, student_exam.gender, student_exam.weight)
    return question,'', answer
def question_7(student_exam):
    question = ' open the file test1.txt and change the weight from your weight to 67'
    
    answer =  "\nwith open('test1.text', 'w') as fd:\n\
    fd.write('name:{0}@age:{1}@gender:{2}@weight:67')\n\
    ".format(student_exam.name,student_exam.age,student_exam.gender)
    return question,'',answer
def question_8(student_exam):
    question = " please read out the content in the test2.txt\n \
 (2) change the weight from 60 to 65 and change age  to your real age\n \
 (3) change weight value to your own weight value\n \
 (4) save the new data back to the test2.text file\n"

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
    question = '  could you do a code when you run your code if you input your name then print out hello <your name> else print "sorry i do not you"\n'
    anwser = "\nwhile 1:\n\
    name = input('please type your name '')\n\
    if name != {0}:\n\
        print('student_sorry i do not you')\n\
    else:\n\
        print('hello {0}')\n\
        ".format(student_exam.name, student_exam.name)
    return question, '' ,anwser
def question_10(student_exam):
    question = ' could you please print out the same element in the following 2 list\n'
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
    question = ' Findind out the minum number in the following list\n'
    question_list = [random.randint(342,4343) for i in range(1,100)]
    answer = str(min(question_list))
    question_list = convert_list2str(question_list)
    
    return question, question_list, answer
#combine two list into one
def question_12(student_exam):
    question = ' Could you please combine following two list together? For instance if the list is a = [1,2,3] and b = [4,5,6] you answer should be c = [1,2,3,4,5,6]\n'
    list_1 = [i for i in range(1,20)]
    list_2 = [i for i in range(21,25)]
    list_1.extend(list_2)
    answer = 'code : list_1.extend(list_2) and the answer shoudl be' + convert_list2str(list_1)
    list_1 = convert_list2str(list_1)
    list_2 = convert_list2str(list_2)
    return question, list_1 + list_2, answer


def question_13(student_exam):
    question = " please remove the first element for the list by following. for instance if the list is a = [1,2,3,4,5]\n then the answer is a = [2,3,4,5]"
    question_list = [random.randint(43,455) for i in range(1,20)]
    previous_question = question_list
    question_list.pop(0)
    answer = convert_list2str(question_list)
    question_list = convert_list2str(previous_question)
    return question, question_list, answer

def question_14(student_exam):
    question = " Could you please append the element presenting below to the following list? for instance if the list is [1,2] and the element is 3 then the result should be [1,2,3]\n"
    question_list = [random.randint(1,4) for i in range(1,3)]
    element =  random.randint(1,20)
    answer = "The sample code is list_a.append(element)"
    question_list = "list_1 = " + convert_list2str(question_list)+'\n' + 'element = ' + str(element)+'\n'
    return question, question_list, answer

def question_15(student_exam):
    question = ' is there any syntax error in the following statement?'
    question_list = 'a = [1,2,3;4]\n \
    del a \n\
    print(a)\n'
    answer = "wrong, pleaese note the simicolon"
    return question, question_list, answer

def question_16(student_exam):
    question = ' is there any syntax error in the following statement?\n'
    question_list = 'if a == 1\n \
    print("hello")'
    answer = "syntax wrong there is no colon after if statement"
    return question, question_list, answer

def question_17(student_exam):
    element = {"int": "{0}".format(random.randint(1,20)), "list": "{0}".format([random.randint(1,2443) for i in range(1,10)]),"dict":"{0}".format({"name":"{0}".format(student_exam.name)}), "float": "1.0"}
    answer = random.choice(list(element))
    question_list = str(element[answer])
    question =  " what is the type of the thing below?\n"
    return question, question_list, answer

def question_18(student_exam):
    question = " Could you print out the average value of following list?\n"
    question_list = [random.randint(43,434) for i in range(1,random.randint(23,45))]
    answer = sum(question_list) / len(question_list)
    question_list = convert_list2str(question_list)
    answer = str(answer)
    return question, question_list, answer
def question_19(student_exam):
    question = " could you remove all of the duplicate value in the following list?\n"
    question_list = [random.randint(43,434) for i in range(1,random.randint(23,42))]
    answer = convert_list2str(list(set(question_list)))
    question_list = convert_list2str(question_list)
    return question, question_list, answer
def my_minus(list_1, list_2):
    return list_1 - list_2
def question_20(student_exam):
    question = " Could you please minus each element one by one in the following lists?\n"
    list_1 = [random.randint(43,5356) for i in range(1,343)]
    list_2 = [random.randint(43,5356) for i in range(1,343)]
    answer = map(my_minus,list_1, list_2)
    answer = convert_list2str(answer)
    list_1 = convert_list2str(list_1)
    list_2 = convert_list2str(list_2)
    return question,list_1 + '\n' + list_2, answer
def question_21(student_exam):
    question = " write code change all character in the following string from lower case to upper case\n"
    question_list = ("{0}".format(random.choices(string.ascii_lowercase, k=1)[0])) * 100
    answer = question_list.upper()
    return question, question_list,answer
def question_22(student_exam):
    question = " write code change all character in the following string from upper case to lower case\n"
    question_list = ("{0}".format(random.choices(string.ascii_uppercase, k=1)[0])) * 100
    answer = question_list.upper()
    return question,question_list,answer
def question_23(student_exam):
    question = "Could you please find out all the word 'info' in the following string there is no case sensitive"
    question_list = "[infomation, info INFO, infomative Info iNfo iNFO iNfOmative InFomation andinfo]"
    answer = "you need to use regular expression to do it:\n re.findall('\binfo\b',str,flag=re.I)\n [info,INFO, Info, INFO]"
    return question,question_list,answer
def question_24(student_exam):
    question = "Could you sort the following list by the length of each element?"
    question_list = ["fdasf","feqff","feqwfag","hterr","rqdcc","qfergr4gewgergegr","cxvbvdgfbfbgferbdf","dfeqegreh45tbebtr","r34rfet4537resffy"] * 100
    question_list = convert_list2str(question_list)
    answer = "Hint: question_list.sort(func=myfunc) \n def myfunc(e):\n    return(len(e))"
    return question,question_list,answer
def question_25(student_exam):
    question = "Could you sort the following list by the date?"
    question_list = []
    for i in range(1,100):
        question_str = "fdskjfjdsakjfkadsjfklsd,{} {} {}".format(random.randint(1,31),random.randint(3,12),random.randint(1990,2099)) 
    question_list.append(question_str)
    question_list = convert_list2str(question_list)
    answer = "Hint: question_list.sort(func=myfunc) \n def myfunc(e):\n   here you need to covert your date to number and return"
    return question,question_list,answer
def question_26(student_exam):
    question = "Could you generate a random list with random  int element and random list length?"
    question_list = ""
    answer = "import random\n [random.randint(1,10000) for i in range(1,random.randint(1,100))]"
    return question,question_list,answer
def question_27(student_exam):
    question = "Could you please find the second max number in the following list?"
    question_list = [random.randint(1,100) for i in range(1,random.randint(1,100))]
    question_list = convert_list2str(question_list)
    answer = "question_list.sort()[-2]"
def question_28(student_exam):
    question = "Could you find out the second min number in the following list?"
    question_list = [random.randint(1,100) for i in range(1,random.randint(1,100))]
    question_list = convert_list2str(question_list)
    answer = "question_list.sort()[1]"
def question_29(student_exam):
    question = " Fetch all of the even number in the following string and save them in the list please print them out\n"
    question_list = [(random.randint(1,1000)) for i in range(1,10000)]
    answer = [str(even_number) for even_number in question_list if even_number % 2 == 0]
    question_list = [str(element) for element in question_list]
    question_3_str = '%'.join(question_list)
    answer = '[' + ','.join(answer) + ']'
    return question, question_3_str,answer

def question_30(student_exam):
    question = " Fetch all of the  number can be fully divide by 3 in the following string and save them in the list please print them out\n"
    question_list = [(random.randint(1,1000)) for i in range(1,10000)]
    answer = [str(even_number) for even_number in question_list if even_number % 3 == 0]
    question_list = [str(element) for element in question_list]
    question_3_str = '%'.join(question_list)
    answer = '[' + ','.join(answer) + ']'
    return question, question_3_str,answer

def question_31(student_exam):
    question = "Can you sort the following list by the 5th character in each element?"
    question_list = ["fjkasdjfkwqlf","hwgreqeawqljgierqgh","ortejhgot","grewjigjriowegkweng","grjeoijqopjgfwqeogner","gjorgejr5gabfjad"]
    answer = "def myfunc(e):\n    return e[4]\n question_list.sort(key=myfunc)"
    question_list = convert_list2str(question_list)
    return question, question_list, answer

def question_32(student_exam):
    question = "Can you remove the all of the element in the dictionary?"
    question_list = "my_dict = {'a': {}, 'b':{}, 'c':{}, 'faf':{}}".format(random.randint(1,1000),random.randint(1,1000), random.randint(1,1000),random.randint(1,1000))
    answer = "del my_dict"
    return question, question_list, answer
    
def question_33(stuent_exam):
    question = "Can you sort the following list by the numbers in the []?"
    question_list = ["fasdkfjkdsa [{}]".format(random.randint(332,43452)),"afafqev [{}]".format(random.randint(32,4763)),"brwebgrewe [{}]".format(random.randint(32,43433)),"vaerfvrehre [{}]".format(random.randint(32,4133)),"bsvaa [{}]".format(random.randint(32,243254))]
    answer = "def myfunc(e):\n    msg = e.split(" ")[1]\n    return msg[1]"
    question_list = convert_list2str(question_list)
    return question, question_list, answer
def question_34(student_exam):
    question = "Could you find out all all word start with pre?"
    question_list = "previous apple preoccupy pear preread prepare and also get the sample pre-skill"
    answer = "re.findall('(pre\w+)',question_list)" 
    return question, question_list, answer

def question_35(student_exam):
    question = "Could you get the middle value in the follow list? for instance a = [1,2,3,4,5] then 3 is the middle value"
    question_list =  [random.randint(1,45) for i in range(1,1000)]
    question_list = convert_list2str(question_list)
    answer = "question_list[len(question_list)//2]"
    return question, question_list, answer
              
def question_36(student_exam):
    question = "Could you combine following two list into one? for intance [1,2,3]  [4,5,6] => [1,2,3,4,5,6]"    
    question_list = "a = [345,3,4325,,432] b = [343,6534,7,87,3654,654]"
    answer = "a.extend(b)"
    return question, question_list, answer

def question_37(student_exam):
    question = "Could you get the result of 1 * 2 * 3 * .... 100?"
    question_list = ""
    answer = "result = 1\nfor i in range(1,101):\n    result = result * i"
    return question, question_list, answer

def question_38(student_exam):
    question = "Could you generate a list with all even number in range(1,1000)?"
    question_list = ""
    answer = "[i for i in range(1,1001) if i % 2 == 0] "
    return question, question_list, answer
    
    
              
    
    
    
#Questions2 = [question_1, question_2, question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10, question_11,  question_12, question_13, question_14, question_15, question_16, question_17,question_18,question_19,question_20]
Questions = { \
    'Entry':[    question_1, \
                  question_2, \
                  question_3, \
                  question_4, \
                  question_5, \
                  question_6, \
                  question_7, \
                  question_15, \
                  question_17, \
                  question_18, \
                  question_27,  \
                  question_30,  \
                  question_29, \
                  question_32, \
                  question_36 \
   ], \
    "Intermediate":[question_11, \
                     question_12, \
                     question_13, \
                     question_14, \
                     question_8, \
                     question_21, \
                     question_22,\
                     question_23, \
                     question_24, \
                     question_35 \ 
                    ],\
    "Master": [ question_16, \
                 question_9, \
                 question_10, \
                 question_19, \
                 question_20, \
                 question_25, \
                 question_26,  \
                 question_31, \
                 question_33, \
                 quesntion_34 \
              ] \
}


level_dict = {"1":"Entry","2":"Intermediate","3":"Master"}    

def generate_examination(student_exam, question_for_test):
    final_examine = ''
    final_answer = ''
    for num,q in enumerate(question_for_test):
        question, question_list, answer = q(student_exam)
        final_examine = final_examine  +  str(num + 1) + '.' + question + question_list + '\n\n'
        final_answer =   final_answer  +  str(num + 1) + '.' + question + question_list + "\nThe answer is:" + answer + '\n\n' 
    with open("Examination.txt",'w',encoding='utf-8') as fd:
        fd.write(student_exam.header + final_examine)
    with open("Answer.txt",'w',encoding='utf-8') as fd:
        fd.write(student_exam.header + final_answer)
    print("Test and answer code Generated done! Enjoy ^_^")

if  __name__ == "__main__":
    while 1:
        student_name   = input("Please input your name: ")
        student_age    = input("please input your age: ")
        student_gender = input ("please input your gender: ")
        student_weight = input ("please input your weight: ")
        student_exam = student_examination(student_name, student_gender,student_age,student_weight) 
       # student_exam = student_examination('Jack', 'male',10,80)
        level = input("please select question level (type 1,2,3):\n\
        (1).Entry\n\
        (2).Intermediate\n\
        (3).Master\n")
        if level in level_dict:
            question_for_test = np.random.choice(Questions[level_dict[level]], size = Amount_of_question, replace = False)
            random.shuffle(question_for_test)
            break
        elif level == 'test':
            all_question = []
            for value in Questions.values():
                all_question.extend(value)
                print(all_question)
            question_for_test = np.random.choice(all_question, size=Amount_of_question, replace=False)
            random.shuffle(question_for_test)
            break
        else:
            print("please type 1,2,3 to get your level")

        #student_exam = student_examination('Jack', 'male',10,80)
    generate_examination(student_exam, question_for_test)
    
