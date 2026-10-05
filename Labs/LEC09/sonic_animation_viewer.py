# LEC09 소닉 애니메이션 뷰어
# sonic-sprite.png (소닉 스프라이트 시트)로 캐릭터 애니메이션을 재생한다.
# - 대기 / 걷기 / 달리기 / 구르기 / 스핀볼 / 질주 / 슈퍼필아웃 / 스프링점프 / 3D달리기 / 승리포즈 10종 (총 76프레임)
# - 1200x800 해상도 화면 정중앙에서 각 애니메이션을 5회 반복 재생한 뒤 마지막 프레임에서 1초 정지하고 다음 애니메이션으로 전환한다.
# - 모든 애니메이션을 차례로 무한 반복하며, ESC 키 입력 또는 창 닫기로 안전하게 종료한다.

from pico2d import *
import pico2d
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
# 애니메이션 이름 표시용 폰트 (pico2d 내장 폰트)
FONT_PATH = os.path.join(os.path.dirname(pico2d.__file__), 'data', 'ConsolaMalgun.ttf')

# 01. 대기 및 기본 모션 (IDLE) - 11프레임
IDLE_FRAMES = [
    (1, 39, 29, 39),
    (31, 40, 26, 38),
    (58, 39, 27, 39),
    (85, 40, 30, 38),
    (115, 40, 33, 38),
    (150, 40, 30, 38),
    (182, 40, 29, 38),
    (211, 39, 28, 38),
    (239, 39, 30, 38),
    (270, 45, 24, 32),
    (302, 51, 29, 26),
]

# 02. 걷기 (WALK) - 12프레임
WALK_FRAMES = [
    (8, 80, 26, 37),
    (37, 80, 27, 37),
    (65, 80, 31, 38),
    (97, 80, 37, 37),
    (135, 80, 32, 35),
    (170, 79, 32, 38),
    (206, 79, 26, 38),
    (238, 80, 24, 37),
    (263, 80, 30, 37),
    (295, 80, 36, 37),
    (334, 80, 32, 36),
    (370, 79, 29, 38),
]

# 03. 달리기 (RUN) - 6프레임
RUN_FRAMES = [
    (1, 124, 33, 40),
    (39, 124, 35, 39),
    (89, 125, 35, 38),
    (130, 121, 34, 42),
    (181, 122, 34, 41),
    (228, 122, 33, 40),
]

# 04. 구르기 / 스핀 (ROLL) - 9프레임
ROLL_FRAMES = [
    (1, 169, 29, 30),
    (35, 167, 29, 31),
    (67, 169, 30, 29),
    (98, 169, 31, 29),
    (131, 168, 29, 30),
    (162, 168, 29, 31),
    (193, 170, 30, 29),
    (230, 170, 31, 29),
    (268, 170, 30, 30),
]

# 05. 스핀 볼 (SPIN BALL) - 6프레임
SPIN_BALL_FRAMES = [
    (1, 206, 30, 27),
    (36, 206, 29, 27),
    (70, 206, 29, 27),
    (105, 206, 29, 27),
    (139, 206, 29, 27),
    (174, 206, 29, 27),
]

# 06. 질주 / 필아웃 (PEELOUT) - 6프레임
PEELOUT_FRAMES = [
    (1, 239, 29, 35),
    (36, 239, 30, 35),
    (74, 239, 31, 35),
    (111, 238, 31, 36),
    (149, 239, 30, 35),
    (186, 238, 31, 36),
]

# 07. 슈퍼 필아웃 (SUPER PEELOUT) - 6프레임
SUPER_PEELOUT_FRAMES = [
    (1, 283, 29, 35),
    (36, 283, 30, 35),
    (72, 286, 39, 31),
    (123, 285, 39, 32),
    (172, 286, 39, 31),
    (218, 285, 38, 32),
]

# 08. 스프링 점프 회전 (SPRING JUMP) - 8프레임
SPRING_JUMP_FRAMES = [
    (1, 326, 24, 45),
    (31, 327, 29, 44),
    (65, 327, 20, 44),
    (90, 327, 25, 43),
    (119, 327, 25, 43),
    (149, 327, 20, 44),
    (184, 341, 40, 28),
    (232, 341, 39, 27),
]

# 09. 3D 정면 달리기 (3D RUN) - 8프레임
RUN_3D_FRAMES = [
    (1, 379, 27, 38),
    (31, 379, 31, 36),
    (64, 379, 31, 36),
    (99, 377, 33, 38),
    (136, 379, 32, 36),
    (176, 379, 33, 36),
    (217, 379, 33, 36),
    (254, 378, 33, 36),
]

# 10. 승리포즈 및 피격 (WIN & HURT) - 4프레임
WIN_HURT_FRAMES = [
    (6, 429, 34, 40),
    (49, 426, 34, 43),
    (96, 427, 23, 39),
    (125, 427, 23, 39),
]

# 재생할 10종 애니메이션 목록 (이름, 프레임 하나당 시간(초), 프레임 리스트)
ANIMATIONS = [
    ('IDLE', 0.08, IDLE_FRAMES),
    ('WALK', 0.07, WALK_FRAMES),
    ('RUN', 0.06, RUN_FRAMES),
    ('ROLL', 0.04, ROLL_FRAMES),
    ('SPIN BALL', 0.04, SPIN_BALL_FRAMES),
    ('PEELOUT', 0.04, PEELOUT_FRAMES),
    ('SUPER PEELOUT', 0.04, SUPER_PEELOUT_FRAMES),
    ('SPRING JUMP', 0.06, SPRING_JUMP_FRAMES),
    ('3D RUN', 0.06, RUN_3D_FRAMES),
    ('WIN & HURT', 0.12, WIN_HURT_FRAMES),
]


def draw_frame(frame):
    # frame = (left, top, width, height) - 시트 좌상단 기준 좌표
    left, top, width, height = frame
    # pico2d 좌하단 기준 bottom 좌표로 변환
    bottom = SHEET_HEIGHT - (top + height)
    sonic.clip_draw(left, bottom, width, height,
                    CENTER_X, CENTER_Y,
                    width * SCALE, height * SCALE)


def draw_label(name, count):
    font.draw(30, CANVAS_HEIGHT - 40, f'{name}  {count + 1}/{REPEAT_COUNT}', (255, 255, 255))


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
            draw_label(name, count)
            update_canvas()
            delay(frame_time)

    # 반복이 끝나면 마지막 프레임을 보여준 채로 정지
    wait(PAUSE_TIME)


def main():
    global sonic, font, running

    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    sonic = load_image(SPRITE_PATH)
    font = load_font(FONT_PATH, 28)

    running = True

    # 모든 애니메이션을 차례로 재생하는 것을 종료할 때까지 무한 반복
    while running:
        for name, frame_time, frames in ANIMATIONS:
            play_animation(name, frame_time, frames)
            if not running:
                break

    close_canvas()


if __name__ == '__main__':
    main()
