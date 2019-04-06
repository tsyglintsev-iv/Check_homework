#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 3.Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#    name — строка, полученная от пользователя,
#    health = 100,
#    damage = 50.


users = {
    "player": {
        "name": "Maxik",
        "health": 100,
        "damage" : 50
    },
    "enemy": {
        "name": "Boris",
        "health": 100,
        "skype": 50
    }
}



print(users["player"])
