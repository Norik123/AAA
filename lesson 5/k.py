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

арпарпрополлоролролролролрол

x1=int(input("Идти налево или направо?(пример:+3 или -3)"))
y1=int(input("Идти вверх или вниз?(пр.:+3 или -3)"))

if x1>0:
    sprite.change_sprite_costume(monster,"enemy_blue_right1")

if x1<0:
    sprite.change_sprite_costume(monster,"enemy_blue_left1")

sprite_actions.move_sprite_to(monster,1500,monsterx+x1,monstery)


if y1>0:
    sprite.change_sprite_costume(monster,"enemy_blue_down1")

if y1<0:
    sprite.change_sprite_costume(monster,"enemy_blue_up1")

a=monsterx+x1
b=monstery+y1
sprite_actions.move_sprite_to(monster,1500,a,b)


x2=int(input("Идти налево или направо?(пример:+3 или -3)"))
y2=int(input("Идти вверх или вниз?(пр.:+3 или -3)"))
if x2>0:
    sprite.change_sprite_costume(monster,"enemy_blue_right1")

if x2<0:
    sprite.change_sprite_costume(monster,"enemy_blue_left1")

sprite_actions.move_sprite_to(monster,1500,a+x2,b)


if y2>0:
    sprite.change_sprite_costume(monster,"enemy_blue_down1")

if y2<0:
    sprite.change_sprite_costume(monster,"enemy_blue_up1")

sprite_actions.move_sprite_to(monster,1500,a+x2,b+y2)
