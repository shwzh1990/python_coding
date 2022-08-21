import json
import numpy as np
import random
import os
questions_amount = 5
def level():
    num = input("please select different level: \n 1.Easy \n 2.Intermetiate\n 3.Hard\n 4.Random\n")
    return num
def Selection_func():
    count = 0
    current_question_num = 1
    while 1:
        num = level()
        with open("Mori_Dictionary.json", 'r', encoding="utf-8") as fd:
            data = json.load(fd)
        if num not in data.keys() and num != '4':
            print("please type the number in [1-4]")
            continue
        question_dict = {}
        if num != '4':
            questions_list = np.random.choice([key for key in data[num].keys()], questions_amount, replace=False)
        else:
            question_total = []
            for key in data.keys():
                question_total.extend(list(data[key].keys()))
            questions_list = np.random.choice(question_total, questions_amount, replace=False)
        for question_key in questions_list:
            if num != '4':
                question_dict[question_key] = data[num][question_key]
            else:
                for a in data.keys():
                    if question_key in data[a].keys():
                        question_dict[question_key] = data[a][question_key]
        for question in question_dict.keys():
            answer_list = [question_dict[question]]
            if num != '4':
                answer_list.extend(np.random.choice(
                    [fake_answer for fake_answer in data[num].values() if fake_answer != question_dict[question]], 3,
                    replace=False))
            else:
                answer_list.extend(np.random.choice(
                    [fake_answer for fake_answer in data[str(random.randint(1, 3))].values() if fake_answer != question_dict[question]], 3, replace=False))
            random.shuffle(answer_list)
            map_dict = {"A": answer_list[0], "B": answer_list[1], "C": answer_list[2], "D": answer_list[3]}
            answer = input("Question{}.{}\n".format(current_question_num,question) + "    A.{}\n    B.{}\n    C.{}\n    D.{}\n".format(answer_list[0], answer_list[1], answer_list[2], answer_list[3]) + "please input the answer:")
            if answer not in ["a", "A", "b", "B", "C", 'c', "D", 'd']:
                print("please type the answer in A-D no case sensitive")
                continue
            answer = answer.capitalize()
            if map_dict[answer] == question_dict[question]:
                count = count + 100 / questions_amount
            else:
                print("The Answer should be {}\n".format(answer))
                go = input("press any key to continue!")
            os.system("cls")
            current_question_num = current_question_num + 1
        print("The test is Done! \n The finnal result is {}".format(count))
        count = 0
        break
def Word_Answer():
    count = 0
    current_question_num = 1
    question_dict = {}
    with open("Mori_Dictionary.json", 'r', encoding="utf-8") as fd:
        data = json.load(fd)
    while 1:
        os.system("cls")
        num = level()
        if num not in data.keys() and num != '4':
            print("please type the number in [1-4]")
            continue
        if num != "4":
            for answer, question in data[num].items():
                question_dict[question] = answer
            question_list = np.random.choice([question for question in question_dict.keys()], questions_amount,replace=False)
        else:
            question_total = []
            for key in data.keys():
                question_total.extend(data[key].values())
                for answer, question in data[key].items():
                    question_dict[question] = answer
            question_list = np.random.choice(question_total, questions_amount, replace=False)
        for question in question_list:
            answer = input("Question{}.".format(current_question_num) + question + ": ")
            if answer == question_dict[question]:
                print("Correct!!\n")
                count = count + 100 / questions_amount
            else:
                print("The correct answer is {}".format(question_dict[question]))
            current_question_num = current_question_num + 1
        print("Your final score is {}".format(count))
        break
def Add_vocabulary():
    with open("Mori_Dictionary.json", 'r', encoding="utf-8") as fd:
        data = json.load(fd)
    while 1:
        os.system("cls")
        key = input("please input your Mori vocabulary: ")
        if key == "q":
            with open("Mori_Dictionary.json", "w", encoding="utf-8") as fd:
                json.dump(data, fd, indent=4)
                break
        answer_value = input("please write your answer in English meaning:")
        level = input("Which level do you want to set?\n1.Easy\n2.Intermediate\n3.Hard\n")
        if int(level) not in [i for i in range(1,4)]:
            print("please select the level from [1 - 3]")
            continue
        data[level][key] = answer_value
questions_type = {"1": Selection_func, "2": Word_Answer, "3":Add_vocabulary}
def menu():
    print("Welcome To Our Maori Test!")
    typing_num = input("please input which question type you want:\n1.MultiSelection\n2.Word Answer\n3.Add Vocabulary\n")
    os.system("cls")
    questions_type[typing_num]()
menu()