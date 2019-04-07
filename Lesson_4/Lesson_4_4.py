#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 3.Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#    name — строка, полученная от пользователя,
#    health = 100, здоровье сущности
#    damage = 50, урон, уоторый нанносит сущность
#    armor  = 1.2 коэффициент снижения урона от врага

player = "Кузьма"
enemy = "Борис"

users = {
    player: {
        "name": player,
        "health": 1000,
        "damage": 50,
        "armor": 1.2
    },
    enemy: {
        "name": enemy,
        "health": 100,
        "damage": 50,
        "armor" : 1.99
    }
}

def armoring (damage, armor):
    return (damage / armor)


def fight(attacker, defender):
    defender["health"] = round (defender["health"] - armoring(attacker["damage"], defender["armor"]) )
    print('{} атаковал {} и оставил ему {} здоровья'.format(attacker['name'], defender['name'], defender['health']))


fight(users[player], users[enemy]) #Игрок бьёт по врагу
fight(users[enemy], users[player]) #Вражина отвечает
