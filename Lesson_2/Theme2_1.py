#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Удалите из первого списка элементы, присутствующие во втором.

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

r = len(my_list_2)


for x in range(r):
#    print ("my_list_2", "[x]" "=", my_list_2[x])

    i=0
    while i < len(my_list_1):
        if (my_list_1[i] == my_list_2[x]):
#            del my_list_1[i]
            my_list_1.pop(i)
        else:
            i=i+1

print(my_list_1)


