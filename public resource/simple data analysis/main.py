import random
name = ['Jack,gender:male',"lisa,gender:female",'Tom,gender:male',\
        'Marry,gender:female',\
        "Jim,gender:male",\
        "Julian,gender:male",\
        'Jason,gender:male',\
        'Jenson,gender:male',\
        "robot,gender:male",\
        'kevin,gender:male',\
        'kim,gender:male',\
        'kimmy,gender:male',\
        'rob,gender:male',\
        'Tywin,gender:male',\
        'Javad,gender:male',\
        'william,gender:male',\
        'James,gender:male',\
        'Henry,gender:male',\
        'Victor,gender:male',\
        'Charlise,gender:male',\
        'Zac,gender:male',\
       "Iris,gender:female",\
        'Coco,gender:female',\
        'Lily,gender:female',\
        'Lucy,gender:female']
courses = ['Chinese','Math','English','GYM']


student_num = 123456
year = 2021
data_info = []
for i in range(0,student_num+1):
    student_info_list = []
    ID = year * student_num + i
    student_info_list.append("ID:"+str(ID))
    student_name = name[random.randint(0,len(name)-1)]
    student_info_list.append('Name:' + student_name)
    for course in courses:
        student_info_list.append(course+':'+str(random.randint(10,100)))
    student_str = ','.join(student_info_list)+'\n'
    data_info.append(student_str)
with open('student_info.txt','w') as f:
    f.writelines(data_info)
