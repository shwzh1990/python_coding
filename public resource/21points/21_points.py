import numpy as np
import time
import random
My_Card = []

def convert2digit_sum(cards:list) -> int:
    my_list = []
    for card in cards:
        print(card[1:])
        my_list.append(int(card[1:]))
    return sum(my_list)

def computer_check(My_Cards:list,cards:list) -> bool:
    total_amount = convert2digit_sum(cards)
    print("Total_amount {0}".format(total_amount))
    if total_amount > 21:
        return False
    else:
        Threshold = 21 - total_amount
        less_than_threshold_list = [i for i in My_Cards if int(i[1:]) <= Threshold]
        if len(less_than_threshold_list)/len(My_Cards) < 0.55:
              return True
    return False

def play_card():
    human_list = []
    My_Card = ["A{0}".format(i) for i in range(1,14)]
    My_Card.extend(["B{0}".format(i) for i in range(1,14)])
    My_Card.extend(["C{0}".format(i) for i in range(1,14)])
    My_Card.extend(["D{0}".format(i) for i in range(1,14)])
    random.shuffle(My_Card)
    computer_list = []
    while 1:
        card_pickup = np.random.choice(My_Card, 4, replace = False)
        who_serve = input("Please select who serve first:\nPress 1 computer serve first and Press 2 human serve first\n")
        if who_serve == "1":
            computer_list.extend(card_pickup[:2])
            human_list.extend(card_pickup[2:])
        elif who_serve == "2":
            computer_list.extend(card_pickup[2:])
            human_list.extend(card_pickup[:2])
        else:
            print("Please type 1 or 2")
            continue
        My_Card = [i for i in My_Card if i not in card_pickup]   #remove picked up card
        print("human card is {0}, and computer list is {1}".format(human_list,computer_list))
        while 1:
            pick_extra_cards = input("Do you want to get extra cards?Press Y/y to continue and N/n to stop")
            if pick_extra_cards in ['Y','y']:
                new_card = np.random.choice(My_Card,1,replace = False)
                My_Card.remove(new_card)
                human_list.extend(new_card)
                print("Your new card is ", new_card)
            print("Computer select time....")
            time.sleep(1)
            if computer_check(My_Card, computer_list) == True:
                new_card = np.random.choice(My_Card,1,replace = False)
                My_Card.remove(new_card)
                computer_list.extend(new_card)
                print("Computer new card is ", new_card)
                continue
            if computer_check(My_Card, computer_list) == False and pick_extra_cards in ['N',"n"]:
                break
 

        computer_result = convert2digit_sum(computer_list)
        human_result = convert2digit_sum(human_list)
        print("Computer has cards {0}".format(",".join(computer_list)))
        print("Human has cards {0}".format(",".join(human_list)))

        if computer_result == human_result:
            print("DRAW")
        elif computer_result > 21 and human_result < 21:
            print("Human Wins")
        elif computer_result < 21 and human_result > 21:
            print("Computer Wins")
        elif (computer_result < 21 and human_result < 21 ) or (computer_result > 21 and human_result > 21):
            if computer_result < human_result:
                print("Computer Wins")
            else:
                print("Human Wins")
        status = input("Do you want to play again?\nPress Y to continue and N to exit")
        if status == "Y":
            break
        else:
            exit(0)

def menu():
    input("-----------Welcome to 21 points-----------\n\
          Press Enter to continue....")
    
    play_card()
menu()
    

