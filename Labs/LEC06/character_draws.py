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
        draw_character(x, y)
    
    pass

def move_top():
    print("top")
    for x in range(50, 751, 5):
        draw_character(x, 550)
      

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_right():
    for y in range(550, 49, -5):
        draw_character(750, y)
    pass

def move_bottom():
    for x in range(750, 49, -5):
        draw_character(x, 50)
    pass

def move_left():
    for y in range(50, 551, 5):
        draw_character(50, y)
    pass

def move_tri_right():
    for x in range(100, 701, 5):
        y = 100
        draw_character(x, y)

def move_tri_leftTop():
    for y in range(100, 501, 5):
        x = 700 - (y - 100) * (3/4)
        draw_character(x, y)

def move_tri_leftbottom():
    pass

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_triangle():
    move_tri_right()
    move_tri_leftTop()
    move_tri_leftbottom()
    pass 

##-----------------------------------------------

while True:
    ##move_circle()
    ##move_rectangle()
    move_triangle()
    break
    pass


close_canvas()