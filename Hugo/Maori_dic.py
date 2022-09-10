import json
import os
import numpy as np
def Multiselection():
    while 1:
        mutiselection_Answer = input("What level will you choose?\n1.Easy\n2.Intermediate\n3.Hard\n4.Random\n")
        if mutiselection_Answer == "q":
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
            pass
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
        # print(data)
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