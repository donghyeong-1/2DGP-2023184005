from pico2d import *
import os

CANVAS_WIDTH, CANVAS_HEIGHT = 1200, 800
CENTER_X, CENTER_Y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2

# 캐릭터를 4배 확대하여 출력
SCALE = 4

# 스프라이트 시트 원본 높이 (상단 기준 좌표 변환용)
SHEET_HEIGHT = 525

# 실행 위치와 상관없이 이 파일이 있는 폴더에서 이미지를 찾는다
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPRITE_PATH = os.path.join(BASE_DIR, 'sonic-sprite.png')

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image(SPRITE_PATH)

delay(1)

close_canvas()
