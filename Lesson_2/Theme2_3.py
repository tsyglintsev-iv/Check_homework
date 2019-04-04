#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Дан список заполненный произвольными целыми числами.
#Получите новый список, элементами которого будут только уникальные элементы исходного.

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = []

r = len(my_list_1)

for i in range(r):

    if my_list_1.count(my_list_1[i]) == 1:
       my_list_2.append(my_list_1[i])

print (my_list_2)