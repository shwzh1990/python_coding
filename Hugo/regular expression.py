import re
with open("regular_expression.txt",'r') as fd:
    data = fd.read()

a = re.match(r"ab?","ab",re.M)
if a:
    print(a.group())

a = re.match(r"ab?","a")
print(a.group())


a = re.search(r"(ab+)", data)
if a:
    print(a.group(0))
    print(a.span())

a = re.findall(r"ab+",data)
print(a)

a = re.findall(r"Jack+\s",data)
print(a)

a  = re.findall(r"Jack[1-9]{2,3}",data)
print(a)






import re

data = "abc,abe,ab#,ab!,ab2,ab1,ab3,ab4,ab5"

#? 问号之前的哪个字符可有可无

#abc? => ab / abc
#ab+ => ab abbbb 
#^a
# . => for anything
# \d (0-9)
# \D (none digit)
#[]  match the range in it

find = re.findall(r"Document CHNDLY....................",data)
re.split()
print(find)
























