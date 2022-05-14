import re

with open("CD_all.txt",'r',encoding='utf-8') as fd:
    data = fd.read()

a = re.findall(r"Document CHNDLY...................", data, re.M)
print(len(a))