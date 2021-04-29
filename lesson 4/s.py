import wrap_py.ru, random
from wrap_py import sprite, sprite_actions, world
from random import randint

world.create_world(600, 600)
world.set_world_background_color_rgb(27,195,255)

spot1 = sprite.add_sprite("pacman",
                          randint(1, 600),
                          randint(1, 600),
                          costume="dot")
spot2 = sprite.add_sprite("pacman",
                          x=randint(1, 600),
                          y=randint(1, 600),
                          costume="dot")

hero = sprite.add_sprite("pacman",
                         300,
                         300,
                         costume="player2")

sprite.change_sprite_size_proc(hero, 110, 110)
sprite_actions.rotate_to_point(hero, 1000, sprite.get_sprite_x(spot1), sprite.get_sprite_y(spot1))
sprite_actions.move_sprite_to(hero, 1000, sprite.get_sprite_x(spot1), sprite.get_sprite_y(spot1))
sprite.hide_sprite(spot1)
sprite.change_sprite_size_proc(hero, 130, 130)

sprite_actions.rotate_to_point(hero, 1000, sprite.get_sprite_x(spot2), sprite.get_sprite_y(spot2))
sprite_actions.move_sprite_to(hero, 1000, sprite.get_sprite_x(spot2), sprite.get_sprite_y(spot2))
sprite.hide_sprite(spot2)
sprite.change_sprite_size_proc(hero, 150, 150)

enemy = sprite.add_sprite("pacman",
                          sprite.get_right(hero)+10,
                          sprite.get_top(hero)-10,
                          costume="enemy_red_down1")
sprite.add_text(sprite.get_sprite_x(enemy),(sprite.get_sprite_y(enemy))-30,"Я тебя съем",font_size=13)
sprite_actions.rotate_to_angle(hero,1000,215)
sprite_actions.move_sprite_to_angle(hero,1000,300)
