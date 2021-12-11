#! /usr/bin/env python
#coding=utf-8


num_list = [i for i in range(1,1000)]
num = input("please give a number:")
for number in num_list:
    if num % number == 0:
        print(num)


