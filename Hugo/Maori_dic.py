#import json, random, os and np.
import json
import random
import os
import numpy as np
#def a function of asking what level will the user choose.
def level():
    Level_Answer = input("What level will you choose?\n1.Easy\n2.Intermediate\n3.Hard\n4.Random\n")
    return Level_Answer
#def Multiselection
def Multiselection():
    #a list that containbs all the questions in data

    #define 5 questions
    question_amount = 5
    #a dict that is used to prepared questions and answers together
    question_dict = {}
    #the number of the question
    current_question_num = 1
    #points
    count = 0
    
    while 1:
        #ask a question
        mutiselection_Level = level()
        #turn "Maori_dictionary.json" into a dic.
        with open("Maori_dictionary.json",'r',encoding="utf-8") as fd: 
            data = json.load(fd)
        #correct the user if had typed something unexpected
        if mutiselection_Level not in data and mutiselection_Level != "4":
            warning = input ("please type the answer between 1-4")
        #continue the program without any edits
            continue
        #if user clicks easy level/medium level/hard level, we create a list called question_list to get 5 random questions in the level user typed.
        if mutiselection_Level != "4":
            question_list = np.random.choice([key for key in data[mutiselection_Level].keys()],question_amount,replace = False)
        #if user typed 4, then gather all the questions in all the levels(1,2,3) and randomly choose 5 questions in them.
        else:
            for key in data.keys():
                questions = []
                questions.extend(list(data[key].keys()))
            question_list = np.random.choice(questions,question_amount,replace=False)
        #prepear the 5 questions with their answers in question_dict by using the questions in the level user typed if the user typed 1,2,or 3.
        for question_key in question_list:
            if mutiselection_Level != "4":
                question_dict[question_key] = data[mutiselection_Level][question_key]
        #if not,then prepear the 5 questions with their answers in question_dict by using all of the quesitons in data.
            else:
                for element in data.keys():
                    if question_key in data[element].keys():
                        question_dict[question_key] = data[element][question_key]
        #create a list called answer_list that contains all the answers
        for question in question_dict.keys():
            answer_list = [question_dict[question]]
        #get 3 fake answers in answer_list for each question
            if mutiselection_Level != "4":
                answer_list.extend(np.random.choice([fake_answer for fake_answer in data[mutiselection_Level].values() if fake_answer != question_dict[question]], 3,replace=False))
            else:
                answer_list.extend(np.random.choice([fake_answer for fake_answer in data[str(random.randint(1,3))] if fake_answer != question_dict[question]],3,replace = False))
            random.shuffle(answer_list)
        #set up the question and options
            option_map = {"A" : answer_list[0], "B" : answer_list[1],"C" : answer_list[2], "D" : answer_list[3]}
            user_answer = input("question{}.{}\n".format(current_question_num,question) + " A.{}\n B.{}\n C.{}\n D.{}\n".format(answer_list[0], answer_list[1], answer_list[2], answer_list[3]) + "please input the answer:" ) 
        #correct user if did not typed in a,A,b,B,c,C,d,D.
            if user_answer not in["a","A","b","B","c","C","d","D"]:
                print("please type the answer in A-D no case sensitive")
        #continue the program without any edits
                continue
        #capitalize the first letter of the word"question".
            user_answer = user_answer.capitalize()
        #if the user answered the question correctly, point out and then add 100/question_amount points.
            if option_map[user_answer] == question_dict[question]:
                count = count + 100 / question_amount
                print("You are correct!")
        #if not, then point out and go on to next question
            else:
                print("The Answer should be {}\n".format(question_dict[question]))
                go = input("Please press any key to continue!")
                os.system("cls")
                current_question_num = current_question_num + 1
         #tell the user the test is done and change the points to 0 again.       
        print("The test is Done! \n The finnal result is {}".format(count))
        count = 0
        #break out to finish the program
        break
    
#def word answer
def Word_answer():
    #points
    count = 0
    #how many questions
    question_amount = 5
    #a dict that is used to prepear the questions and the answers
    question_dict = {}
    while 1:
        #turn "Maori_dictionary.json" into a dic
        with open("Maori_dictionary.json","r",encoding = "utf-8") as fd:
            data = json.load(fd)
            word_Level = level()
        #correct user if had typed something unexpected
        if word_Level not in data and word_Level != "4":
            warning = input("Please type the answer between 1-4")
        #continue the program without any edits
            continue
        #if the user had typed the level in 1,2,3, then get all the questions and all the answer in that level
        if word_Level != "4":
            for answer,question in data[word_Level].items():
                question_dict[question] = answer
        #create a list called quesiton_list and extend 5 random questions
            question_list = np.random.choice([question for question in question_dict.keys()],question_amount, replace=False)
        #if the user had typed "4", thenget 5 random questions in data
        elif word_Level == "4":
            question_total = []
            for key in data.keys():
                question_total.extend(data[key].values())
                for answer, question in data[key].items():
                     question_dict[question] = answer
            question_list = np.random.choice(question_total, question_amount, replace=False)
        #set up the question
        i = 1
        for question in question_list:
            Question = input("Question " + str(i) + ":" + question+"\n")
            i = i + 1
        #if the answer was correct, point it out and add 100/question_amount points
            if Question == question_dict[question]:
                print("Correct!\n")
                count = count + 100/question_amount
        #if not, then tell the user
            else:
                print("WRONG ANSWER!"+ "\n" + "The correct answer is {}\n".format(question_dict[question]))
        #give out the user's score end the program
        print("Your final score is {}".format(count))
        #end the program
        break
    
    #def Add_Vocabulary
def Add_Vocabulary():
    #turn "Maori_dictionary.json" into a dic.
    with open("Maori_dictionary.json","r",encoding = "utf-8")as fd:
        data = json.load(fd)
    while 1:
        #to ask the user what level will be their new word appear in.
        level_answer = input("What level is your new word?\n1.Easy\n2.Medium\n3.Hard\n")
        #if the user clicks q button, then save to "Maori_dictionary.json".
        if level_answer == "q":
            with open("Maori_dictionary.json", "w", encoding="utf-8") as fd:
                json.dump(data, fd, indent=4)
            break
        #if the user had typed something unexpected, then correct the user.
        if level_answer not in ["1","2","3"]:
            print("You need to type numbers in 1-3")
            continue
        #match up the new maori word and it's english meaning that the user typed. 
        new_maori_words = input("Please type your new maori word")
        English_meaning = input("Please type the english meaning of the maori word")
        data[level_answer][new_maori_words] = English_meaning
#to run the function that the user want to run. If the user click "q" button, then finish the program.
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