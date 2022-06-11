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


def func(e):
    date_list = []          
    article_list = e.split("\n")
    for num,content in enumerate(article_list):
        if " words" in content:
            date_list.append(article_list[num+1])
            break
    Month_map = {"January":0,"February":31,"March":31+28,"April":31+28+31,"May":31+28+31+30,"June":31+28+31+30+31,"July":31+28+31+30+31+30,"August":31+28+31+30+31+30+31,"September":31+28+31+30+31+30+31+31,"October":31+28+31+30+31+30+31+31+30,"November":31+28+31+30+31+30+31+31+30+31,"December":31+28+31+30+31+30+31+31+30+31+30}  
    for date in date_list:
        date_list = date.split(" ")
    return int(date_list[0]) + int(Month_map[date_list[1]]) + int(date_list[2])*356    
    
    
    
#print(func())
new_article.sort(key=func)

with open("pakistan_all_time.txt", 'w', encoding="utf-8") as fd:
    fd.writelines(new_article)

