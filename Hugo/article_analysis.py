import re
import random

with open("pakistan_all.txt", 'r', encoding='utf-8') as fd:
    data = fd.read()
a = re.findall(r"Document A........................", data, re.M)
a = re.split(r"Document A........................", data)
a.pop()
f = len(a)

new_article = []
for articles in a:
    articles = articles.strip("\n")
    articles = articles.strip()
    new_article.append(articles)
del a

def func(e):
    date_list = []
    article_list = e.split("\n")
    for a,content in enumerate(article_list):
        if word in content:
            date_list.append(article_list[a+1])
            break
    Months = {"January":0,"February":31,"March":31 + 28,"April":31 + 28 + 31,"May":31 + 28 + 31 + 30,"June":31 + 28 + 31 + 30 + 31, "July":31 + 28 + 31 + 30 + 31 + 30, "August":31 + 28 + 31 + 30 + 31 + 30 + 31, "September":31 + 28 + 31 + 30 + 31 + 30 + 31 + 31, "October":31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30,"November":31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31, "December":31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30}
    for dates in date_list:
        b = dates.split(" ")
    return int(b[0]) + int(Months[b[1]]) + int(b[2])*365
new_article.sort(key = func)
with open("pakistan_all_time.txt","w" , encoding="utf-8")as fd:
    fd.writelines(new_article)
###################################################################
#questions that I am gonna ask the teacher:
#1.are we gonna past anything into e?
#2.how to run this function?
#3.how to know thst it check it?


    # result.sort()
    # new_article.sort(key=result)
#     print(result)
#     return lt
# covert_sort_year(new_article)

# print(new_article.sort(key=covert_sort_year))
# new_article.sort(key=covert_sort_year)
# def myFunc(e):
#   return len(e)
#
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
#
# cars.sort(key=myFunc)
#
# print(cars)
#print(new_article)
#Plan:
#1.get the list including all of the article
#2.myfunc=> 1.get the date from e args e reprensent every article 2.covert date to number 3.return number
#3.result.sort(key = myfunc)

# def myfunc(e):
#     return e[1]
# names = ["Asher", "Kayden", "Jyden", "Tom", "Hugo", "Antonia"]
# names.sort(key = myfunc)
# print(names)
# myfunc()
