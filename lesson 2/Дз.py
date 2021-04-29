import wrap_py
from time import sleep
from wrap_py import world,sprite
from wrap_py import sprite_actions
world.create_world(1000,600)

# move_1=world.set_world_background_color_rgb(255,249,38)
# predator=sprite.add_sprite("star_wars",80,500,True,"ship1")
# prey=sprite.add_sprite("star_wars",260,500,True,"x-wing"),sprite.rotate_to_angle(1,90)
# a="Стой"
# b="Неа"

move_2=world.set_world_background_color_rgb(32,221,255)
predator=sprite.add_sprite("star_wars",80,500,True,"x-wing")
sprite.rotate_to_angle(0,90)
prey=sprite.add_sprite("star_wars",260,500,True,"ship1")
a="Теперь я лечу за тобой"
b="АААААААААА"

print(predator)
print(prey)

sleep(1)
sprite.add_text(100,420,a)
sleep(1)
sprite.hide_sprite(2)
sleep(1)
sprite.add_text(260,420,b)
sleep(1)
sprite.hide_sprite(3)
sleep(1)
sprite_actions.move_sprite_to(1,1000,700,500)
sprite_actions.move_sprite_to(0,1000,530,500)
sprite_actions.rotate_to_angle(1,1000,45)
sprite_actions.move_sprite_to_angle(1,1000,300)
sprite_actions.rotate_to_angle(0,1000,65)
sprite_actions.move_sprite_to_angle(0,1000,270)
sprite_actions.rotate_to_angle(1,1000,-45)
sprite_actions.move_sprite_to_angle(1,1000,300)
sprite_actions.rotate_to_angle(0,1000,-15)
sprite_actions.move_sprite_to_angle(0,1000,170)
sprite_actions.rotate_to_angle(1,1000,-90)
sprite_actions.move_sprite_to_angle(1,1000,430)
sprite_actions.rotate_to_angle(0,1000,-60)
sprite_actions.move_sprite_to_angle(0,1000,270)
sprite.add_text(300,150,"Догнал ?")
sleep(1)
sprite.hide_sprite(4)
sleep(1)
sprite.add_text(500,160,"Топливо почти закончилось")
sleep(1)
sprite.hide_sprite(5)





