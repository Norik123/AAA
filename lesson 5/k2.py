import wrap_py.ru, random
from random import randint
from time import sleep
from wrap_py import sprite, sprite_actions, world

world_x = 600
world_y = 600
world.create_world(world_x, world_y)

monsterx = world_x / 2
monstery = world_y / 2
monster = sprite.add_sprite("pacman", monsterx, monstery, costume="enemy_blue_down1")
sprite.change_sprite_size_proc(monster, 180, 180)

x = int(input("Координаты X"))
y = int(input("Координаты Y"))

if x > 0:
    sprite.change_sprite_costume(monster, "enemy_blue_right1")
    sprite_actions.move_sprite_to(monster, 1500, monsterx + x, monstery)
    if y > 0:
        sprite.change_sprite_costume(monster, "enemy_blue_down1")
        sprite_actions.move_sprite_to(monster, 1500, monsterx + x, monstery + y)
    if y < 0:
        sprite.change_sprite_costume(monster, "enemy_blue_up1")
        sprite_actions.move_sprite_to(monster, 1500, monsterx + x, monstery + y)

if x < 0:
    sprite.change_sprite_costume(monster, "enemy_blue_left1")
    sprite_actions.move_sprite_to(monster, 1500, monsterx + x, monstery)
    if y > 0:
        sprite.change_sprite_costume(monster, "enemy_blue_down1")
        sprite_actions.move_sprite_to(monster, 1500, monsterx + x, monstery + y)
    if y < 0:
        sprite.change_sprite_costume(monster, "enemy_blue_up1")
        sprite_actions.move_sprite_to(monster, 1500, monsterx + x, monstery + y)

a = monsterx + x
b = monstery + y

x1 = int(input("Координаты X"))
y1 = int(input("Координаты Y"))

if x1 > 0:
    sprite.change_sprite_costume(monster, "enemy_blue_right1")
    sprite_actions.move_sprite_to(monster, 1500, a + x1, b)
    if y1 > 0:
        sprite.change_sprite_costume(monster, "enemy_blue_down1")
        sprite_actions.move_sprite_to(monster, 1500, a + x1, b + y1)
    if y1 < 0:
        sprite.change_sprite_costume(monster, "enemy_blue_up1")
        sprite_actions.move_sprite_to(monster, 1500, a + x1, b + y1)

if x1 < 0:
    sprite.change_sprite_costume(monster, "enemy_blue_left1")
    sprite_actions.move_sprite_to(monster, 1500, a + x1, b)
    if y1 > 0:
        sprite.change_sprite_costume(monster, "enemy_blue_down1")
        sprite_actions.move_sprite_to(monster, 1500, a + x1, b + y1)
    if y1 < 0:
        sprite.change_sprite_costume(monster, "enemy_blue_up1")
        sprite_actions.move_sprite_to(monster, 1500, a + x1, b + y1)
