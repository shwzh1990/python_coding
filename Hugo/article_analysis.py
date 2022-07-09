import re
import random

with open("pakistan_all.txt", 'r', encoding='utf-8') as fd:
    data = fd.read()
a = re.findall(r"Document A........................", data, re.M)
a = re.split(r"Document A........................", data)
a.pop()
f = len(a)

new_article = []
for article in a:
    article = article.strip('\n')
    article = article.strip()
    new_article.append(article)
del a
# print(new_article[])

def get_article_date():
    i = 0
    d = []
    for i in range(f):
        z = new_article[i].split("\n")
        for b,element in enumerate(z):
            if "words" in element:
                d.append(z[b+1])
                break
get_article_date()

def myfunc(e):
    return e
result = []
c = 0
y = 0
i = 0
d = []
for i in range(f):
    z = d[i].split("\n")
    for b,element in enumerate(z):
        if "words" in element:
            d.append(z[b+1])
            break
i = 0
for i in range(f):
    s = d[i].split()
    c = s[0]
    y = s[1]
    p = s[2]
    v = {
        "January":0,
        "February":31,
        "March":59,
        "April":90,
        "May":120,
        "June":151,
        "July":181,
        "August":212,
        "September":243,
        "October":273,
        "November":304,
        "December":334
        }
    x = int(p) * 365
    result.append(int(c) + v[y] + int(x))

new_article.sort(key=myfunc)
###################################################################
#questions that I am gonna ask the teacher:
#1.are we gonna past anything into e?
#2.how to run this function?
#3.how to know check it?


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
