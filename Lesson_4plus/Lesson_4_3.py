#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 3.Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#    name — строка, полученная от пользователя,
#    health = 100,
#    damage = 50.

player = "Кузьма"
enemy = "Борис"

users = {
    player: {
        "name": player,
        "health": 1000,
        "damage": 50
    },
    enemy: {
        "name": enemy,
        "health": 100,
        "damage": 50
    }
}


def fight(attacker, defender):
    #defender["health"] = (defender["health"] - attacker["damage"])
    defender["health"] -= attacker["damage"] # так тоже можно
    print('{} атаковал {} и оставил ему {} здоровья'.format(attacker['name'], defender['name'],
                                                                      defender['health']))
    # print(defender["health"])


fight(users[player], users[enemy])
# print(users)
fight(users[enemy], users[player])
# print(users)
