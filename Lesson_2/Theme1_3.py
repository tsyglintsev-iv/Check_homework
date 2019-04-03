#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Программа «Медицинская анкета»

print("Медицинская анкета")
name =  input("Введите ваше имя: ")
age =   int(input("Введите ваш возраст: "))
mass = int(input("Введите ваш вес: "))

if (0 <= age <= 30) and (50 <= mass <= 120):
    print("{}, {} год, вес {} кг {}".format(name, age, mass, "- хорошее состояние."))

elif (30 < age < 40) and ((mass > 120) or (mass < 50)):
    print("{}, {} год, вес {} кг {}".format(name, age, mass, "- следует заняться собой."))

elif (age >= 40) and ((mass > 120) or (mass < 50)):
    print("{}, {} год, вес {} кг {}".format(name, age, mass, "- следует обратиться к врачу!"))

else:
    print("Ваше состояние не поддаётся машинному анализу")