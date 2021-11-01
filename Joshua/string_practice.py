string_list = ["www.baidu.com", "shwzh1990@gmail.com","www.google.com","www.my_school.com","jshi@ivent.com",'www.chinacom']

#find email address
for string in string_list:
    if '@' in string:   #if string includes '@'
        print(string)


'''
find website. needs to be start with www. and endwith .com
'''
'''
for string in string_list:
    if string.endswith(".com") == True and string.startswith("www.") == True:
        print(string)
        
'''

'''
practice 3
split
'''
'''
rawstring = "www.baidu.com"
str_list = rawstring.split(".")
print(str_list)
'''
'''
for info in string_list:
    if info.endswith(".com") == True and info.startswith("www.") == True:
        info_list = info.split('.')
        print(info_list[1])
'''

my_string = "Jack marry Lisa Tom joshua hugo"
my_list = my_string.split(" ")
print(my_list)
print(len(my_list))

my_string = "Jack#marry#Lisa#Tom#joshua#hugo"
