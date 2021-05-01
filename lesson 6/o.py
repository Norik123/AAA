import random
from random import randint, choice

player1 = random.choice(["камень", "ножницы", "бумага"])
player2 = random.choice(["камень", "ножницы", "бумага"])

print("у игрока №1 ", player1)
print("у игрока №2 ", player2)

if player1 == player2:
    print("ничья")
    exit()

if player1 != "камень" and player2 != "камень":
    print("ножницы порезали бумагу")
    if player1 == "ножницы":
        print("победа игрока №1")
    else:
        print("победа игрока №2")

if player1 != "ножницы" and player2 != "ножницы":
    print("бумага покрывает камень")
    if player1 == "бумага":
        print("победа игрока №1")
    else:
        print("победа игрока №2")

if player1 != "бумага" and player2 != "бумага":
    print("камень ломает ножницы")
    if player1 == "камень":
        print("победа игрока №1")
    else:
        print("победа игрока №2")
