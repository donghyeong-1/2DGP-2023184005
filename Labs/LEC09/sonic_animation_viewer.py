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


def draw_frame(frame):
    # frame = (left, top, width, height) - 시트 좌상단 기준 좌표
    left, top, width, height = frame
    # pico2d 좌하단 기준 bottom 좌표로 변환
    bottom = SHEET_HEIGHT - (top + height)
    sonic.clip_draw(left, bottom, width, height,
                    CENTER_X, CENTER_Y,
                    width * SCALE, height * SCALE)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image(SPRITE_PATH)

running = True
first_frame = (1, 39, 29, 39)

while running:
    handle_events()
    clear_canvas()
    draw_frame(first_frame)
    update_canvas()
    delay(0.05)
    # 0.5초 후 테스트 종료 (향후 루프로 확장)
    break

close_canvas()
