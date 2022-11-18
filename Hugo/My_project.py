working = 0# a value that will help us later by counting how many lines of informations do we need 
# List = []
import re#To import re, so we can use the re.findall() function to find the rows we need
with open("normal.log","r",encoding="utf-8") as fd:#open normal.log txt as reading mode
    data = fd.read()#give the reading mode a name called "data"
rows = data.split("\n")#split it into rows
x = 0#a varible need to represent every rows later
for each in rows:#start a range
    # print(rows[x])
    y = re.findall("<----.*",each)#find all of the rows we need       
    if "<----" in str(y):#to find out the ys that contains <----
        working = working + 1
        #add 1 to the number of how many lines of informations we need
        # Y = str(y)
        # information = str(Y)
        # information = str(y).split(" ")#to sort the informations so that we can put into our dic later.
        elements = str(y).split(" ")
        Devices = str(elements[1])
        Tests = str(elements[2])
        # Result = str(elements[7])
        Success = "SUCCESS"
        Fail = "ERROR"
        success_number = 0
        fail_numbber = 0
        Results = str(elements[7])
        print(Results)
        # print(Devices)
        dictionary = {}
        print(Devices)
        if len(dictionary) == 0:
            dictionary = { Devices: {Tests :{
                                        Success: success_number,
                                        Fail: fail_numbber}}}
        else:
            if Devices == dictionary[Devices]:
                if Tests == dictionary[Tests]:
                    if Results == Success:
                        success_number = success_number + 1
            else:
                dictionary[Devices][Tests][Success] = success_number

        # print(dictionary)
        # print(elements)
    # print(Result[elements[1]])
        # print(elements[1])
    # print(Result)
        # print(information[1])
        # print(information[2])
        # print(information[7])
        # print(Y)#print them to check
    # if y != []:
    #     working = working + 1
    x = x + 1#to make sure it moves to the next row everytime after checking the row that it just checked
# print(information)
# information.split(" ")

# print(working)
    # print(y)
# print(rows[207])
# y = re.findall(r"<----.*",rows)
# z = re.findall(r"<----.*ERROR",rows)
# print(x)
# print(y)
# List.append(x)
# List.append(y)
# print(List)
# for rows in data:
#     print(rows)
    # if "<----" in rows:
    #     print(rows)
# print(data)
# element = data.split("***************** Next Device *****************")
# element.pop(0)
