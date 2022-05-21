import re

with open("CD_all.txt",'r',encoding='utf-8') as fd:
    data = fd.read()

a = re.findall(r"Document CHNDLY...................", data, re.M)

#print(len(a))
#article = re.split(r"Document CHNDLY...................", data)
#print(len(article))
#import re
##? ab? =>a, ab
##+ ab+ => ab abbb abbbbbb
##. 
##\w any alphabet, character==
##\W 
##\s
##\S
##^  beginning of the string
##[1-5]
#str_sample = "ab,abbhjk, a5,a3,a6,abbcb, abbbjkbbbbbbbbb,a*,a#$%,a!$%$^$%#,a{,a ,"
#result = re.findall("(a[1-5]),",str_sample)
#print(result)
str_sampe = "abdkljfadskl23fjfdkljklfjd45fgjreaklgj56dksjfgklfejr78fjeiejwklflk90fjakldsfjkdl"
result_list = re.split(r"\d\d",str_sampe,re.ASCII)
print(result_list)

