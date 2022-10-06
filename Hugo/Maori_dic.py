import json
import random
import os
import numpy as np

    #select level
def level():
    mutiselection_Answer = input("What level will you choose?\n1.Easy\n2.Intermediate\n3.Hard\n4.Random\n")
    return mutiselection_Answer

def Multiselection():
    questions = []
    question_amount = 5
    question_dict = {}
    current_question_num = 1
    count = 0
    while 1:
        mutiselection_Answer = level()
        with open("Maori_dictionary.json",'r',encoding="utf-8") as fd:
            data = json.load(fd)
    
    #correct user if they type something that is wrong
        if mutiselection_Answer not in data and mutiselection_Answer != "4":
            warning = input ("please type the answer between 1-4")
            continue
    #randomly choose a question and the answer of the question
        if mutiselection_Answer != "4":
            question_list = np.random.choice([key for key in data[mutiselection_Answer].keys()],question_amount,replace = False)
            # print(question_list)
        else:
            for key in data.keys():
                questions.extend(list(data[key].keys()))
            question_list = np.random.choice(questions,question_amount,replace=False)
            # print(question_list)
    #get the correct answers for the 5 questions
        for question_key in question_list:
            if mutiselection_Answer != "4":
                question_dict[question_key] = data[mutiselection_Answer][question_key]
                # print(question_dict)
            else:
                for element in data.keys():
                    if question_key in data[element].keys():
                        question_dict[question_key] = data[element][question_key]
        for question in question_dict.keys():
            answer_list = [question_dict[question]]
            if mutiselection_Answer != "4":
                answer_list.extend(np.random.choice([fake_answer for fake_answer in data[mutiselection_Answer].values() if fake_answer != question_dict[question]], 3,replace=False))
            else:
                answer_list.extend(np.random.choice([fake_answer for fake_answer in data[str(random.randint(1,3))]],3,replace = False))
             #set the questions(like options)
            option_map = {"A" : answer_list[0], "B" : answer_list[1],"C" : answer_list[2], "D" : answer_list[3]}
            user_answer = input("question{}.{}\n".format(current_question_num,question) + " A.{}\n B.{}\n C.{}\n D.{}\n".format(answer_list[0], answer_list[1], answer_list[2], answer_list[3]) + "please input the answer:" ) 
            if user_answer not in["a","A","b","B","c","C","d","D"]:
                print("please type the answer in A-D no case sensitive")
                continue
            user_answer = user_answer.capitalize()
            
            #count up points
            if option_map[user_answer] == question_dict[question]:
                count = count + 100 / question_amount
            else:
                print("The Answer should be {}\n".format(question_dict[question]))
                go = input("press any key to continue!")
                os.system("cls")
                current_question_num = current_question_num + 1
                
        print("The test is Done! \n The finnal result is {}".format(count))
        count = 0
        break
    
def Word_answer():
    random_question_list = {}
    count = 0
    question_amount = 5
    question_dict = {}

    while 1:
        with open("Maori_dictionary.json","r",encoding = "utf-8") as fd:
            data = json.load(fd)
            # print(data)
        word_answer = input("What level will you choose?\n1.Easy\n2.Intermediate\n3.Hard\n4.Random\n")
        if word_answer == "q":
            break
        if word_answer not in data and word_answer != "4":
            warning = input("Please type the answer between 1-4")
            continue
        if word_answer != "4":
            for answer,question in data[word_answer].items():
                question_dict[question] = answer
            question_list = np.random.choice([question for question in question_dict.keys()],question_amount, replace=False)
        elif word_answer == "4":
            question_total = []
            for key in data.keys():
                question_total.extend(data[key].values())
                for answer, question in data[key].items():
                     question_dict[question] = answer
            question_list = np.random.choice(question_total, question_amount, replace=False)
        i = 1
        for question in question_list:
            Question = input("Question " + str(i) + ":" + question+"\n")
            i = i + 1
            if Question == question_dict[question]:
                print("Correct!\n")
                count = count + 100/question_amount
            else:
                print("WRONG ANSWER!"+ "\n" + "The correct answer is {}\n".format(question_dict[question]))
        print("Your final score is {}".format(count))
        break
def Add_Vocabulary():
    with open("Maori_dictionary.json","r",encoding = "utf-8")as fd:
        data = json.load(fd)
    while 1:
        level_answer = input("What level is your new word?\n1.Easy\n2.Medium\n3.Hard\n")
        if level_answer == "q":
            with open("Maori_dictionary.json", "w", encoding="utf-8") as fd:
                json.dump(data, fd, indent=4)
            break
        if level_answer not in ["1","2","3"]:
            print("You need to type numbers in 1-3")
            continue
        new_maori_words = input("Please type your new maori word")
        English_meaning = input("Please type the english meaning of the maori word")
        data[level_answer][new_maori_words] = English_meaning
        # print(data)\
            
            
print("Welcome to the maori test!")
while 1:
    select_menu = input("Please select level: \n1.Multiselection\n2.Word answer\n3.Add vocabulary\n")
    if select_menu == "1":
        Multiselection()
    elif select_menu == "2":
        Word_answer()
    elif select_menu == "3":
        Add_Vocabulary()
    elif select_menu == "q":
        break
    else:
        print("Please type numbers 1-3")