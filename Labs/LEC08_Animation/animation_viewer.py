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

# 대기 (Idle & Bored) - 13프레임
IDLE_FRAMES = [
    (32, 1411, 29, 45, 8, 0), (83, 1411, 30, 45, 7, 0), (134, 1411, 31, 44, 6, 0),
    (186, 1411, 31, 45, 6, 0), (237, 1411, 33, 45, 5, 0), (290, 1411, 32, 45, 6, 0),
    (341, 1411, 33, 45, 5, 0), (392, 1411, 34, 44, 4, 0), (446, 1411, 32, 45, 6, 0),
    (497, 1411, 33, 45, 5, 0), (548, 1411, 34, 44, 4, 0), (600, 1411, 34, 44, 4, 0),
    (650, 1411, 38, 43, 2, 0),
]


def draw_background():
    r, g, b = BACKGROUND_COLOR
    draw_rectangle(0, 0, CANVAS_WIDTH - 1, CANVAS_HEIGHT - 1, r, g, b, 255, True)


def draw_frame(frame):
    left, bottom, width, height, ox, oy = frame
    # 확대된 셀이 화면 중앙에 오도록 셀의 좌하단 위치를 구한다
    cell_x = CENTER_X - CELL_SIZE * SCALE // 2
    cell_y = CENTER_Y - CELL_SIZE * SCALE // 2
    sonic.clip_draw_to_origin(left, bottom, width, height,
                              cell_x + ox * SCALE, cell_y + oy * SCALE,
                              width * SCALE, height * SCALE)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image(SPRITE_PATH)

for frame in IDLE_FRAMES:
    clear_canvas()
    draw_background()
    draw_frame(frame)
    update_canvas()
    delay(0.1)

close_canvas()
