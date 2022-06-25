#password check system
#1. if the password is wrong then give 3 times re-try
#2. if password is correct then print(congraduation)

i = 3
while i:
    password = input("please input your password:")
    if password == "1234":
        print("congraduation")
        i = 0
    else:
        print("your password is wrong please re-try")
        i = i - 1
