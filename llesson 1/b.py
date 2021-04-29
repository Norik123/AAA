from time import sleep
from wrap_py import sprite,world
import wrap_py.ru
wrap_py.world.create_world(500,500)
world.set_world_background_color_rgb(178,58,131)
wrap_py.sprite.add_sprite("blue_man",500,100)
sleep(3)
sprite.add_sprite("star_wars",10,40)
sprite.add_sprite("star_wars",30,20,1,"ship3")
sprite.add_text(70,80,"Hello")