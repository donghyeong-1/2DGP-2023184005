from pico2d import *
import os

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
CENTER_X, CENTER_Y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2

# 시트에 투명 배경이 없어서 프레임 셀의 배경색으로 화면을 채운다
BACKGROUND_COLOR = (13, 72, 7)

# 실행 위치와 상관없이 이 파일이 있는 폴더에서 이미지를 찾는다
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPRITE_PATH = os.path.join(BASE_DIR, 'gold_sonic_sprite.png')


def draw_background():
    r, g, b = BACKGROUND_COLOR
    draw_rectangle(0, 0, CANVAS_WIDTH - 1, CANVAS_HEIGHT - 1, r, g, b, 255, True)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image(SPRITE_PATH)

clear_canvas()
draw_background()
update_canvas()
delay(1.0)

close_canvas()
