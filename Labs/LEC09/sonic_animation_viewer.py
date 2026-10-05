from pico2d import *
import os

CANVAS_WIDTH, CANVAS_HEIGHT = 1200, 800
CENTER_X, CENTER_Y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2

# 캐릭터를 4배 확대하여 출력
SCALE = 4

# 애니메이션 하나를 반복하는 횟수
REPEAT_COUNT = 5
# 반복이 끝난 뒤 다음 애니메이션까지 정지하는 시간(초)
PAUSE_TIME = 1.0

# 스프라이트 시트 원본 높이 (상단 기준 좌표 변환용)
SHEET_HEIGHT = 525

# 실행 위치와 상관없이 이 파일이 있는 폴더에서 이미지를 찾는다
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPRITE_PATH = os.path.join(BASE_DIR, 'sonic-sprite.png')

# 01. 대기 (IDLE) - 8프레임
IDLE_FRAMES = [
    (1, 39, 29, 38),
    (31, 40, 26, 38),
    (58, 39, 58, 39),
    (118, 40, 30, 38),
    (150, 40, 30, 38),
    (182, 39, 87, 39),
    (270, 45, 24, 31),
    (302, 51, 29, 25),
]

# 02. 걷기 (WALK) - 12프레임
WALK_FRAMES = [
    (8, 80, 26, 37),
    (37, 80, 25, 36),
    (65, 80, 31, 38),
    (97, 80, 37, 36),
    (135, 80, 32, 35),
    (170, 79, 32, 37),
    (206, 79, 26, 38),
    (238, 80, 24, 37),
    (263, 80, 30, 37),
    (295, 80, 35, 36),
    (334, 80, 32, 36),
    (370, 79, 29, 38),
]

# 03. 달리기 (RUN) - 6프레임
RUN_FRAMES = [
    (2, 124, 32, 39),
    (40, 124, 34, 38),
    (90, 125, 34, 37),
    (130, 121, 34, 41),
    (181, 122, 34, 41),
    (228, 122, 32, 39),
]

# 04. 질주 (PEELOUT) - 8프레임
PEELOUT_FRAMES = [
    (1, 169, 29, 30),
    (35, 167, 29, 31),
    (67, 169, 30, 29),
    (98, 169, 31, 29),
    (131, 168, 29, 30),
    (162, 168, 29, 31),
    (193, 170, 30, 29),
    (230, 170, 31, 29),
]

# 05. 구르기 (ROLL) - 5프레임
ROLL_FRAMES = [
    (1, 206, 30, 27),
    (36, 206, 29, 27),
    (70, 206, 29, 27),
    (105, 206, 29, 27),
    (139, 206, 29, 27),
]

# 06. 스핀대시 (SPIN DASH) - 6프레임
SPIN_DASH_FRAMES = [
    (1, 239, 29, 34),
    (36, 239, 30, 34),
    (75, 239, 30, 35),
    (111, 238, 31, 35),
    (149, 239, 30, 35),
    (186, 238, 31, 35),
]

# 07. 밀기 (PUSH) - 6프레임
PUSH_FRAMES = [
    (1, 283, 29, 34),
    (36, 283, 30, 34),
    (72, 286, 39, 31),
    (123, 285, 39, 32),
    (172, 286, 39, 31),
    (218, 285, 38, 32),
]

# 08. 제동 (SKID) - 8프레임
SKID_FRAMES = [
    (1, 326, 24, 44),
    (31, 329, 29, 41),
    (65, 328, 20, 42),
    (90, 328, 25, 42),
    (119, 328, 25, 42),
    (149, 328, 20, 42),
    (184, 341, 39, 28),
    (232, 341, 38, 26),
]

# 09. 점프 (JUMP) - 8프레임
JUMP_FRAMES = [
    (1, 379, 27, 38),
    (31, 379, 31, 36),
    (64, 379, 31, 36),
    (99, 377, 33, 38),
    (136, 379, 32, 35),
    (176, 379, 33, 36),
    (217, 379, 33, 36),
    (254, 378, 33, 36),
]

# 10. 승리포즈 (WIN POSE) - 9프레임
WIN_POSE_FRAMES = [
    (6, 429, 34, 39),
    (49, 426, 34, 42),
    (96, 427, 23, 38),
    (125, 427, 23, 38),
    (33, 9, 15, 23),
    (49, 9, 13, 23),
    (63, 9, 13, 23),
    (78, 3, 21, 29),
    (112, 2, 35, 30),
]

# 재생할 10종 애니메이션 목록 (이름, 프레임 하나당 시간(초), 프레임 리스트)
ANIMATIONS = [
    ('IDLE', 0.08, IDLE_FRAMES),
    ('WALK', 0.07, WALK_FRAMES),
    ('RUN', 0.06, RUN_FRAMES),
    ('PEELOUT', 0.04, PEELOUT_FRAMES),
    ('ROLL', 0.04, ROLL_FRAMES),
    ('SPIN DASH', 0.04, SPIN_DASH_FRAMES),
    ('PUSH', 0.09, PUSH_FRAMES),
    ('SKID', 0.06, SKID_FRAMES),
    ('JUMP', 0.06, JUMP_FRAMES),
    ('WIN POSE', 0.08, WIN_POSE_FRAMES),
]


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


def wait(seconds):
    # delay 한 번으로 오래 멈추면 그동안 창을 닫을 수 없으므로
    # 짧게 나누어 기다리면서 이벤트를 계속 처리한다
    end_time = get_time() + seconds
    while running and get_time() < end_time:
        handle_events()
        delay(0.01)


def play_animation(name, frame_time, frames):
    for count in range(REPEAT_COUNT):
        for frame in frames:
            handle_events()
            if not running:
                return
            clear_canvas()
            draw_frame(frame)
            update_canvas()
            delay(frame_time)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image(SPRITE_PATH)

running = True

for name, frame_time, frames in ANIMATIONS:
    play_animation(name, frame_time, frames)
    if not running:
        break

close_canvas()
