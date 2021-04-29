import wrap_py.ru, random
from random import randint
from time import sleep
from wrap_py import sprite, sprite_actions, world

a=randint(1,1)
b=input("Какое число?")
if a==int(b):
    print("Угадал")
    exit()
else:
    print("Не угадал")

    b=input("Какое число?")
    if a==int(b):
        print("Угадал")

    else:
        print("Не угадал")


        b=input("Какое число?")
        if a==int(b):
            print("Угадал")
        else:
            print("Не угадал")

