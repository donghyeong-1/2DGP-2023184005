from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
CENTER_X, CENTER_Y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

clear_canvas()
update_canvas()
delay(1.0)

close_canvas()
