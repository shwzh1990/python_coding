import re
import random
with open("pakistan_all.txt",'r',encoding='utf-8') as fd:
    data = fd.read()
a = re.findall(r"Document A........................", data, re.M)
a = re.split(r"Document A........................", data)
a.pop()

new_article = []

for article in a:
    article = article.strip('\n')
    article = article.strip()
    new_article.append(article)
del a


def func():
    date_list = []
    for article in new_article:
        temp_article_list = article.split("\n")
        if temp_article_list[0] == "Editorial":
            date_list.append(temp_article_list[4])  
        date_list.append(temp_article_list[4]) 
         
    print(date_list) 
    

#new_article.sort(key=func)
func()

'''
   1. find out all of the date scentence and doing the sorting by using the func in the sort function
'''

