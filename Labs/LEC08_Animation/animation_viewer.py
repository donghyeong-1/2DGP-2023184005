from pico2d import *
import os

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
CENTER_X, CENTER_Y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2

# 원본 캐릭터가 약 45px로 작아서 화면의 절반 이상을 차지하도록 확대한다
SCALE = 8

# 시트에 투명 배경이 없어서 프레임 셀의 배경색으로 화면을 채운다
BACKGROUND_COLOR = (13, 72, 7)

# 실행 위치와 상관없이 이 파일이 있는 폴더에서 이미지를 찾는다
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPRITE_PATH = os.path.join(BASE_DIR, 'gold_sonic_sprite.png')

# 시트의 프레임 한 칸(셀)은 48x48이지만 실제 캐릭터 크기는 프레임마다 다르다.
# 그래서 프레임마다 캐릭터가 차지하는 영역만 잘라서 쓴다.
# 프레임 = (left, bottom, width, height, ox, oy)
#   left, bottom, width, height : pico2d 좌표(좌하단 원점) 기준 잘라낼 영역
#   ox, oy : 셀 좌하단에서 잘라낸 영역까지의 거리 (프레임끼리 발 위치를 맞추는 용도)
CELL_SIZE = 48

IDLE_FIRST_FRAME = (32, 1411, 29, 45, 8, 0)


def draw_background():
    r, g, b = BACKGROUND_COLOR
    draw_rectangle(0, 0, CANVAS_WIDTH - 1, CANVAS_HEIGHT - 1, r, g, b, 255, True)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image(SPRITE_PATH)

clear_canvas()
draw_background()
left, bottom, width, height, ox, oy = IDLE_FIRST_FRAME
sonic.clip_draw(left, bottom, width, height, CENTER_X, CENTER_Y, width * SCALE, height * SCALE)
update_canvas()
delay(1.0)

close_canvas()
