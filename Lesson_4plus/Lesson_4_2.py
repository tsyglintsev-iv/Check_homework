#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def maxit(num1, num2, num3):    #Наша функция
    numbers = [num1, num2, num3]
    max=0
    for x in numbers:
        print(x)
        if x>max:
            max = x

    return max

print(f"Наибольшее число из трёх - {maxit(309,5,30)}")