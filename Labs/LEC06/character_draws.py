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
    for x in range(400, 751, 5):
        draw_boy(x, 100)

def move_right():
    for y in range(100, 501, 5):
        draw_boy(750, y)

def move_bottom():
    for x in range(750, 49, -5):
        draw_boy(x, 500)

def move_left():
    for y in range(500, 99, -5):
        draw_boy(50, y)

def move_finish():
    for x in range(50, 401, 5):
        draw_boy(x, 100)

def move_tri_right():
    for x in range(100, 701, 5):
        y = 100
        draw_boy(x, y)

def move_tri_leftTop():
    for y in range(100, 501, 5):
        x = 700 - (y - 100) * (3/4)
        draw_boy(x, y)

def move_tri_leftbottom():
    for y in range(500, 99, -5):
        x = 400 - (500 - y) * (3/4)
        draw_boy(x, y)

def move_circle():
    centerX = 400
    centerY = 300
    radius = 200

    for degree in range(270, 631):
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
    move_finish()
    pass

def move_triangle():
    move_tri_right()
    move_tri_leftTop()
    move_tri_leftbottom()
    pass 

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()