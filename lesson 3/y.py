import wrap_py
from wrap_py import sprite,sprite_actions,world
wide=1000
height=150
island1=200
island2=300

world.create_world(wide,height)

y1=(height/4)*3
x1=32
sprite.add_sprite("mario-items",x1,y1,True,"moving_platform2")

x2=wide-32
y2=y1-40
sprite.add_sprite("mario-items",x2,y1,True,"moving_platform2")
mario=sprite.add_sprite("mario-1-big",x1,y2,True,"stand")


half_way=(x2-x1)/2
sprite_actions.move_sprite_to(mario,1000,x1+half_way,y2-half_way)
sprite_actions.move_sprite_to(mario,1000,x2,y2)