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

# 걷기 (Basic Motion) - 8프레임
WALK_FRAMES = [
    (29, 1236, 39, 46, 5, 0), (81, 1237, 39, 44, 5, 1), (137, 1236, 27, 44, 9, 0),
    (190, 1236, 28, 46, 10, 0), (30, 1184, 37, 46, 6, 0), (82, 1185, 38, 43, 6, 1),
    (137, 1184, 27, 44, 9, 0), (188, 1184, 28, 46, 8, 0),
]

# 스핀대시 (Spin-Dash) - 6프레임
SPIN_DASH_FRAMES = [
    (272, 967, 29, 27, 13, 0), (324, 967, 29, 27, 13, 0), (376, 967, 29, 27, 13, 0),
    (428, 967, 29, 27, 13, 0), (480, 967, 29, 27, 13, 0), (532, 967, 30, 27, 13, 0),
]

# 점프 (Rolling and Jumping) - 5프레임
JUMP_FRAMES = [
    (33, 1068, 30, 30, 9, 0), (85, 1068, 30, 30, 9, 0), (137, 1068, 30, 30, 9, 0),
    (189, 1068, 30, 30, 9, 0), (241, 1068, 30, 30, 9, 0),
]

# 달리기 (Full Speed) - 4프레임
RUN_FRAMES = [
    (470, 1237, 37, 36, 5, 1), (522, 1238, 37, 35, 5, 2),
    (470, 1185, 37, 35, 5, 1), (522, 1186, 37, 34, 5, 2),
]

# 피격 (Hurt) - 2프레임, 머리카락이 셀 왼쪽 밖으로 나와 있어 ox가 음수
HURT_FRAMES = [
    (509, 247, 45, 34, -6, 0), (567, 248, 45, 34, -6, 1),
]

# 재생할 애니메이션 목록 (이름, 프레임 하나당 시간(초), 프레임 리스트) - 이 순서대로 재생한다
# 동작마다 자연스러운 속도가 달라서 프레임 시간을 따로 준다
ANIMATIONS = [
    ('IDLE', 0.10, IDLE_FRAMES),
    ('WALK', 0.09, WALK_FRAMES),
    ('SPIN DASH', 0.05, SPIN_DASH_FRAMES),
    ('JUMP', 0.06, JUMP_FRAMES),
    ('RUN', 0.07, RUN_FRAMES),
    ('HURT', 0.15, HURT_FRAMES),
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


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def play_animation(frame_time, frames):
    for count in range(5):
        for frame in frames:
            handle_events()
            if not running:
                return
            clear_canvas()
            draw_background()
            draw_frame(frame)
            update_canvas()
            delay(frame_time)

    # 5회 반복이 끝나면 마지막 프레임을 보여준 채로 1초 정지
    delay(1.0)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image(SPRITE_PATH)

running = True

# 모든 애니메이션을 차례로 재생하는 것을 종료할 때까지 무한 반복
while running:
    for name, frame_time, frames in ANIMATIONS:
        play_animation(frame_time, frames)
        if not running:
            break

close_canvas()
