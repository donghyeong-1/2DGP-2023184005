from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')


def draw_character(x, y):
	clear_canvas()
	character.draw(x, y)
	update_canvas()
	delay(0.01)


def move_circle():
	center_x = 400
	center_y = 300
	radius = 200

	for degree in range(270, 631):
		theta = math.radians(degree)
		x = center_x + radius * math.cos(theta)
		y = center_y + radius * math.sin(theta)
		draw_character(x, y)


def move_rectangle():
	for x in range(400, 751, 5):
		draw_character(x, 100)
	for y in range(100, 501, 5):
		draw_character(750, y)
	for x in range(750, 49, -5):
		draw_character(x, 500)
	for y in range(500, 99, -5):
		draw_character(50, y)
	for x in range(50, 401, 5):
		draw_character(x, 100)


def move_triangle():
	for x in range(400, 701, 5):
		draw_character(x, 100)
	for y in range(100, 501, 5):
		x = 700 - (y - 100) * (3 / 4)
		draw_character(x, y)
	for y in range(500, 99, -5):
		x = 400 - (500 - y) * (3 / 4)
		draw_character(x, y)
	for x in range(100, 401, 5):
		draw_character(x, 100)


while True:
	move_circle()
	move_rectangle()
	move_triangle()


close_canvas()
