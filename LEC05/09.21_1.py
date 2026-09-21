from pico2d import *

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90

while True:
    while x < 779:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 2
        delay(0.01)

    while y < 554:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y += 2
        delay(0.01)

    while x > 21:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x -= 2
        delay(0.01)

    while y > 90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y -= 2
        delay(0.01)

update_canvas()
##delay(5)
close_canvas()