import random
from random import randint


guess = randint(1, 20)
ab= int(input("Какое число(от 1 до 20)?"))


if guess == ab:
    print("Угадал")
    exit()


if guess >= 10:
    print("Между 10 и 20")
    c = int(input("Какое число ?"))
    if guess == c:
        print("Угадал")
    if guess != c:
        if guess >= 15:
            print("Между 15 и 20")
            d = int(input("Какое число ?"))
            if guess == d:
                print("Угадал")
            if guess != d:
                print("Не угадал")
        if guess < 15:
            print("Между 10 и 14")
            e = int(input("Какое число ?"))
            if guess == e:
                print("Угадал")
            if guess != e:
                print("Не угадал")



if guess < 10:
    print("Между 1 и 9")
    f = int(input("Какое число ?"))
    if guess == f:
        print("Угадал")
    if guess != f:
        if guess >= 5:
            print("Между 5 и 9")
            s = int(input("Какое число ?"))
            if guess == s:
                print("Угадал")
            if guess != s:
                print("Не угадал")
        if guess < 5:
            print("Между 1 и 4")
            q = int(input("Какое число ?"))
            if guess == q:
                print("Угадал")
            if guess != q:
                print("Не угадал")
