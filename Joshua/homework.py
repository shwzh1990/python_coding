'''
string = "Jack is a boy"
#1 how to open a file
file = open("first.txt",'w')
#w means i will write the data into this file, and if the file does exist create the file
# 'w' erase all the data in the file.
#3 how to write something into the file
file.write(string)
#2 how to close a file
file.close()
'''
'''
#how to append string in the txt file?
file = open("first.txt","a")  #append string at the end of the file
file.write("and Joshua is a boy as well")
file.close()
'''
'''
#how to read data from txt file
file = open("first.txt", 'r') #read data from file
data = file.read()
print(data)
file.close()
'''
'''
with open("first.txt",'r') as file:
    data = file.read()
print(data)
'''
'''
list_info = ["Joshua is a boy\n","Lisa is a girl\n", "Tom is a boy\n"]
with open("first.txt",'w') as f:
    f.writelines(list_info)
with open("first.txt", 'r') as f:
    data = f.readlines()
print(data)
'''

'''
question 1
could you write '1 + 1 =' into the homework_11_8_2021.txt file?

question 2 
could you append "2" at the end of the '1 + 1 = ' 

questions 3
for a string = "438957 + 34578493 =" could you use python code to get the answer of it and write the string and the answer into the homework_11_8_2021.txt?
the format should be '438957 + 34578493 = 35,017,450'

think about the string split
'''