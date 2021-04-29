import wrap_py.ru, random
from random import randint
from time import sleep
from wrap_py import sprite, sprite_actions, world

world_x = 500
world_y = 500
world.create_world(world_x, world_y)
world.set_world_background_color_rgb(27, 195, 255)

mario = sprite.add_sprite("mario-1-big",
                          80,
                          80,
                          costume="stand")

x1 = int(input("Куда идем?"))
y1 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x1,y1)
sprite.add_sprite("pacman",x1,y1, costume="dot")
print("точка №1 ",x1,y1)
sprite.add_text(x1,y1-8,"точка №1",font_size=12)

x2 = int(input("Куда идем?"))
y2 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x2,y2)
sprite.add_sprite("pacman",x2,y2, costume="dot")
print("точка №2 ",x2,y2)
sprite.add_text(x2,y2-8,"точка №2",font_size=12)

x3 = int(input("Куда идем?"))
y3 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x3,y3)
sprite.add_sprite("pacman",x3,y3, costume="dot")
print("точка №3 ",x3,y3)
sprite.add_text(x3,y3-8,"точка №3",font_size=12)

x4 = int(input("Куда идем?"))
y4 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x4,y4)
sprite.add_sprite("pacman",x4,y4, costume="dot")
print("точка №4 ",x4,y4)
sprite.add_text(x4,y4-8,"точка №4",font_size=12)

x5= int(input("Куда идем?"))
y5 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x5,y5)
sprite.add_sprite("pacman",x5,y5, costume="dot")
print("точка №5 ",x5,y5)
sprite.add_text(x5,y5-8,"точка №5",font_size=12)

treasure=sprite.add_sprite("mario-items",randint(1,world_x),randint(1,world_y),costume="pipe")
sprite.change_sprite_size_proc(treasure,38,38)


