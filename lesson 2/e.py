import wrap_py
from time import sleep
from wrap_py import world,sprite
from wrap_py import sprite_actions
world.set_world_background_color_rgb(108,255,45)
world.create_world(900,600)

# hunter="blue_man"
# victim="flappy_bird"
# hunter_text="Птичка стой"

hunter="flappy_bird"
victim="blue_man"
hunter_text="Иди ты"

sprite.add_sprite(hunter,150,400)
sprite.add_sprite(victim,400,400)
sprite.add_text(150,430,hunter_text)
sleep(2)
sprite.hide_sprite(2)
sprite_actions.move_sprite_to(1,2000,550,400)
sprite_actions.move_sprite_to(0,200,400,400)
sprite_actions.rotate_to_angle(1,1000,45)
sprite_actions.move_sprite_to_angle(1,2000,100)


