import wrap_py.ru, random
from wrap_py import sprite, sprite_actions, world
from random import randint
from time import sleep

world_x = 500
world_y = 500
world.create_world(world_x, world_y)

monsterx = randint(world_x / 2, world_x)
monstery = world_y / 2
monster1 = sprite.add_sprite("pacman", monsterx, monstery, costume="enemy_blue_down1")

x1 = int(input("Введите размер первого монстра(размер в процентах) ?"))
y1 = int(input("Введите размер первого монстра(размер в процентах) ?"))

sprite.change_sprite_size_proc(monster1, x1, y1)
sleep(1)


monster2 = sprite.add_sprite("pacman", monsterx, monstery - 30, costume="enemy_red_down1")
sprite.change_sprite_size_proc(monster2, x1 / 2, y1 / 2)
sprite.move_sprite_to(monster2, monsterx, sprite.get_top(monster1) - (sprite.get_sprite_height(monster2) / 2))
sleep(1)


monster3 = sprite.add_sprite("pacman", monsterx, monstery + 60, costume="enemy_yellow_down1")
sprite.change_sprite_size_proc(monster3, x1 * 2, y1 * 2)
sprite.move_sprite_to(monster3, monsterx, sprite.get_bottom(monster1) + (sprite.get_sprite_height(monster3) / 2))
sleep(1)


packman = sprite.add_sprite("pacman", monsterx - 100,monstery,costume="player2")
x2=sprite.get_sprite_width(monster3)
y2=sprite.get_bottom(monster3) - sprite.get_top(monster2)
sprite.change_sprite_size(packman, x2 / 2, y2 / 5)
sprite.add_text(monsterx - 100, sprite.get_top(packman) - 20, "Аaaaaaaa",
                text_color=(255, 252, 24))
sleep(1)
sprite.hide_sprite(4)


# point = (monsterx - 100,monstery )
# sprite.calc_angle_by_point(monster1, point)
#
# sprite_actions.rotate_to_angle(monster1, 1000, sprite.set_final_angle)


sprite_actions.rotate_to_point(monster2,1000,monsterx-100,monstery)
sprite_actions.rotate_to_point(monster1,1000,monsterx-100,monstery)
sprite_actions.rotate_to_point(monster3,1000,monsterx-100,monstery)

sprite_actions.move_sprite_to(monster2,1000,monsterx-100,monstery)
sprite_actions.move_sprite_to(monster1,1000,monsterx-100,monstery)
sprite_actions.move_sprite_to(monster3,1000,monsterx-100,monstery)

sprite.hide_sprite(packman)
