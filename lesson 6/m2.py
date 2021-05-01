import wrap_py.ru, random, math
from wrap_py import sprite, sprite_actions, world
from random import randint, choice
from time import sleep

world.create_world(1000, 430)
world.set_world_background_color_rgb(27, 195, 255)

mario = sprite.add_sprite("mario-1-big", 450, 400, costume="stand")

Home1 = sprite.add_sprite("mario-items", 200, 150, costume="pipe")
sprite.add_text(200, 80, "1", font_size=50)
Home2 = sprite.add_sprite("mario-items", 500, 150, costume="pipe")
sprite.add_text(500, 80, "2", font_size=50)
Home3 = sprite.add_sprite("mario-items", 800, 150, costume="pipe")
sprite.add_text(800, 80, "3", font_size=50)

FIRE = sprite.add_sprite("pacman", 320, 400, costume="enemy_red_down1")
WATER = sprite.add_sprite("pacman", 360, 400, costume="enemy_blue_down1")
MEAL = sprite.add_sprite("pacman", 400, 400, costume="enemy_yellow_down1")

fire = random.choice(["дом №1", "дом №2", "дом №3"])
water = random.choice(["дом №1", "дом №2", "дом №3"])
meal = random.choice(["дом №1", "дом №2", "дом №3"])

if fire == "дом №1":
    sprite_actions.move_sprite_to(FIRE, 1000, 140, 150)
if fire == "дом №2":
    sprite_actions.move_sprite_to(FIRE, 1000, 440, 150)
if fire == "дом №3":
    sprite_actions.move_sprite_to(FIRE, 1000, 740, 150)

if water == "дом №1":
    sprite_actions.move_sprite_to(WATER, 1000, 200, 210)
if water == "дом №2":
    sprite_actions.move_sprite_to(WATER, 1000, 500, 210)
if water == "дом №3":
    sprite_actions.move_sprite_to(WATER, 1000, 800, 210)

if meal == "дом №1":
    sprite_actions.move_sprite_to(MEAL, 1000, 260, 150)
if meal == "дом №2":
    sprite_actions.move_sprite_to(MEAL, 1000, 560, 150)
if meal == "дом №3":
    sprite_actions.move_sprite_to(MEAL, 1000, 860, 150)

sprite.add_text(450, 350, "В какой дом идем?", font_size=30)
sleep(2)
sprite.hide_sprite(10)


# result = int(input("В какой дом идем?(напишу номер дома)"))
#
# if result == 1:
#     sprite_actions.move_sprite_to(mario, 5000, 200, 150)
# if result == 2:
#     sprite_actions.move_sprite_to(mario, 5000, 500, 150)
# if result == 3:
#     sprite_actions.move_sprite_to(mario, 5000, 800, 150)


sleep(2)
if fire == water == meal == "дом №1":
    sprite_actions.move_sprite_to(mario, 5000, 200, 150)
elif fire == water == meal == "дом №2":
    sprite_actions.move_sprite_to(mario, 5000, 500, 150)
elif fire == water == meal == "дом №3":
    sprite_actions.move_sprite_to(mario, 5000, 800, 150)


elif fire == water == "дом №1" and meal != "дом №1":
    sprite_actions.move_sprite_to(mario, 5000, 200, 150)
elif fire == meal == "дом №1" and water != "дом №1":
    sprite_actions.move_sprite_to(mario, 5000, 200, 150)
elif water == meal == "дом №1" and fire != "дом №1":
    sprite_actions.move_sprite_to(mario, 5000, 200, 150)

elif fire == meal == "дом №2" and water != "дом №2":
    sprite_actions.move_sprite_to(mario, 5000, 500, 150)
elif fire == water == "дом №2" and meal != "дом №2":
    sprite_actions.move_sprite_to(mario, 5000, 500, 150)
elif water == meal == "дом №2" and fire != "дом №2":
    sprite_actions.move_sprite_to(mario, 5000, 500, 150)

elif fire == meal == "дом №3" and water != "дом №3":
    sprite_actions.move_sprite_to(mario, 5000, 800, 150)
elif fire == water == "дом №3" and meal != "дом №3":
    sprite_actions.move_sprite_to(mario, 5000, 800, 150)
elif water == meal == "дом №3" and fire != "дом №3":
    sprite_actions.move_sprite_to(mario, 5000, 800, 150)

else:
    sprite_actions.move_sprite_to(mario, 5000, 800,150)
