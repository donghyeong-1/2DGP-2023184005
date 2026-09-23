# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

def draw_boy(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_top():
    for x in range(50, 751, 5):
        draw_boy(x, y)

def move_right():
    draw_boy(x, y)

def move_bottom():
    draw_boy(x, y)

def move_left():
    draw_boy(x, y)

def move_circle():
    centerX = 400
    centerY = 300
    radius = 200

    for degree in range(360):
        theta = math.radians(degree)
        x = centerX + radius * math.cos(theta)
        y = centerY + radius * math.sin(theta)

        draw_boy(x, y)
    pass

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_triangle():

    pass 

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()