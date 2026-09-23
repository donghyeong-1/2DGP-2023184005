# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')



def move_circle():
    centerX = 400
    centerY = 300
    radius = 200

    for degree in range(360):
        theta = math.radians(degree)
        x = centerX + radius * math.cos(theta)
        y = centerY + radius * math.sin(theta)

        clear_canvas()
        character.draw(x, y)
        update_canvas()

        delay(0.01)
    pass

def move_rectangle():

    pass

def move_triangle():

    pass 

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()