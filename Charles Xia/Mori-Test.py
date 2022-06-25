def Word_answer():
    print("word answer is called")

def Multi_Select():
    print("Multi_select is called")

def memu():
    print("Welcome to my Mori Word Test!!")
    print("Please select test type:")
    select = input("1. Multi_Select\n2. Word answer\n")
    if select == '1':
        Multi_Select()
    elif select == '2':
        Word_answer()
    else:
        print("The number you type is invalid")





memu()
