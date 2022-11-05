#declare a var for save the temp result
'''
result = 0

#step 1: open math file
with open("math.txt",'r') as fd:
    data = fd.readlines()
#step 2: get first element in data
a = data[0]
#step 3: use split to get each element in first caculator
b = a.split(" ")
first = int(b[0])
second = b[1]
third = int(b[2])
#step 4: check b[1] sympol
if second == '-':
    result = first - third

#step 5: combine the list back to str with new result
b[3] = "= " + str(result) + "\n"
print(b[3])

#step 6: write all back
new_answer = " ".join(b)
print(new_answer)
with open("math_anwser.txt","w") as fd:
    fd.write(new_answer)
'''
answer = []
def get_result(my_list):
    if my_list[1] == "-":
        return int(my_list[0]) - int(my_list[2])
    if my_list[1]  == "+":
        return int(my_list[0]) + int(my_list[2])
    if my_list[1] == "*":
        return int(my_list[0]) * int(my_list[2])
    if my_list[1] == "/":
        return int(my_list[0]) / int(my_list[2])

with open("math.txt",'r') as fd:
    data_list = fd.readlines()

for element in data_list:
    my_list = element.split(" ")
    result = get_result(my_list)
    my_list[3] = "= " + str(result) + "\n"   #"=\n" => "= XXX\n"
    new_result = " ".join(my_list)
    answer.append(new_result)

with open("math_answer.txt",'w') as fd:
    fd.writelines(answer)