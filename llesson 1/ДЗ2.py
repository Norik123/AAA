from time import sleep
from wrap_py import sprite,world
import wrap_py.ru
world.create_world(630,600)
world.set_world_background_color_rgb(65,255,252)
sleep(3)
sprite.add_sprite("blue_man",150,450)
sleep(3)
sprite.add_sprite("rocket_man",500,430)
sleep(2)
sprite.add_text(150,320,"Привет")
sleep(2)
sprite.add_text(500,320,"Привет")
sleep(3)
sprite.add_text(150,280,"Как дела ?")
sleep(3)
sprite.add_text(500,280,"Хорошо)А у тебя как ?")
sleep(4)
sprite.add_text(150,240,"Тоже все хорошо.Спасибо")
