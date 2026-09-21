from pico2d import *

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

radius = 200
center_x = 400
center_y = 300
angle = 0

x = 200
y = 300

while True:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()

        angle += 2

        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))

        delay(0.01)

update_canvas()
##delay(5)
close_canvas()