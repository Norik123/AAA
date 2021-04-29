import wrap_py
from wrap_py import sprite,sprite_actions,world
from time import sleep

world_x=600
world_y=700


world.create_world(world_x,world_y)
world.set_world_background_color_rgb(223,225,255)

x1=32
y1=(world_y/4)*3
sprite.add_sprite("mario-items",x1,y1,True,"moving_platform2")


x2=(world_x/8)*3
y2=y1-50
sprite.add_sprite("mario-items",x2,y2,True,"moving_platform2")



x3=(world_x/8)*5
y3=y1+50
sprite.add_sprite("mario-items",x3,y3,True,"moving_platform2")



x4=world_x-32
y4=y1-200
sprite.add_sprite("mario-items",x4,y4,True,"moving_platform2")


mario_x=32
mario_y=y1-40
mario=sprite.add_sprite("mario-1-big",mario_x,mario_y,True,"stand")


mario_way1=(x2-x1)/2
sprite_actions.move_sprite_to(mario,1000,mario_x+mario_way1,mario_y-mario_way1)
sprite_actions.move_sprite_to(mario,1000,x2,y2-40)


mario_way2=(x3-x2)/2
sprite_actions.move_sprite_to(mario,1000,x2+mario_way2,(y2-40)-mario_way2)
sprite_actions.move_sprite_to(mario,1000,x3,y3-40)


mario_way3=(x4-x3)/2
sprite_actions.move_sprite_to(mario,1000,x3+mario_way3,(y3-40)-mario_way3)
sprite_actions.move_sprite_to(mario,1000,x4,y4-40)


sprite.set_sprite_flipx_reverse(mario,True)
words=sprite.add_text(x4-30,(y4-40)-50,"Так,обратно")
sleep(1)
sprite.hide_sprite(words)


mario_way4=(x4-x1)/2
sprite_actions.move_sprite_to(mario,1000,x4-mario_way4,(y4-40)-mario_way4)
sprite_actions.move_sprite_to(mario,1000,mario_x,mario_y)


words2=sprite.add_text(mario_x+20,mario_y-50,"Ну вот")
sleep(1)
sprite.hide_sprite(words2)





