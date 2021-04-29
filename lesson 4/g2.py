import wrap_py.ru, random,math
from wrap_py import sprite, sprite_actions, world
from random import randint
from time import sleep

world_x = 500
world_y = 500
world.create_world(world_x, world_y)
world.set_world_background_color_rgb(27, 195, 255)

mario = sprite.add_sprite("mario-1-big",
                          80,
                          80,
                          costume="stand")

treasure_x=randint(1, world_x)
treasure_y=randint(1, world_y)
treasure1 = sprite.add_sprite("mario-items", treasure_x,treasure_y,False,costume="pipe")
sprite.change_sprite_size_proc(treasure1,33,33)

dist0=math.dist([80,80],[treasure_x,treasure_y])
print(int(dist0),"до клада")
sprite_actions.rotate_to_point(mario,1000,treasure_x,treasure_y)

x1 = int(input("Куда идем?"))
y1 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x1, y1)
sprite.add_sprite("pacman", x1, y1, costume="dot")
text1 = str(x1)
text11 = str(y1)
sprite.add_text(x1, y1 - 20,"x:"+text1+" y:"+text11, font_size=12)
# sprite.add_text(x1, y1 - 8, text11, font_size=12)
sprite_actions.rotate_to_point(mario,1000,treasure_x,treasure_y)

dist=math.dist([x1,y1],[treasure_x,treasure_y])

result=sprite.sprites_collide(mario,treasure1)
if result:
    print("нашел")
    exit()

print(int(dist),"до клада")

x2 = int(input("Куда идем?"))
y2 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x2, y2)
sprite.add_sprite("pacman", x2, y2, costume="dot")
text2 = str(x2)
text22 =  str(y2)
sprite.add_text(x2, y2 - 20, text2, font_size=12)
sprite.add_text(x2, y2 - 8, text22, font_size=12)
sprite_actions.rotate_to_point(mario,1000,treasure_x,treasure_y)

x3 = int(input("Куда идем?"))
y3 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x3, y3)
sprite.add_sprite("pacman", x3, y3, costume="dot")
text3 = str(x3)
text33 =  str(y3)
sprite.add_text(x3, y3 - 20, text3, font_size=12)
sprite.add_text(x3, y3 - 8, text33, font_size=12)
sprite_actions.rotate_to_point(mario,1000,treasure_x,treasure_y)

x4 = int(input("Куда идем?"))
y4 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x4, y4)
sprite.add_sprite("pacman", x4, y4, costume="dot")
text4 = str(x4)
text44 = str(y4)
sprite.add_text(x4, y4 - 20, text4, font_size=12)
sprite.add_text(x4, y4 - 8, text44, font_size=12)
sprite_actions.rotate_to_point(mario,1000,treasure_x,treasure_y)

x5 = int(input("Куда идем?"))
y5 = int(input("Куда идем?"))

sprite_actions.move_sprite_to(mario, 1000, x5, y5)
sprite.add_sprite("pacman", x5, y5, costume="dot")
text5 = str(x5)
text55 =  str(y5)
sprite.add_text(x5, y5 - 20, text5, font_size=12)
sprite.add_text(x5, y5 - 8, text55, font_size=12)
sprite_actions.rotate_to_point(mario,1000,treasure_x,treasure_y)

treasure2=sprite.add_sprite("mario-items", treasure_x,treasure_y,costume="pipe")
sprite.change_sprite_size_proc(treasure2,33,33)

