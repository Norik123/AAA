import wrap_py
from time import sleep
from wrap_py import world,sprite
from wrap_py import sprite_actions
world.create_world(600,600)
sprite.add_sprite("blue_man",200,400)
sleep(3)
sprite.move_sprite_to(0,400,400)
sprite.set_sprite_flipx_reverse(0,True)
sprite_actions.move_sprite_to(0,5000,400,200)
sprite.set_sprite_flipx_reverse(0,False)
