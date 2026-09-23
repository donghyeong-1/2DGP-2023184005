# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')


def move_circle():

    clear_canvas()
    character.draw(400, 300)
    update_canvas()
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