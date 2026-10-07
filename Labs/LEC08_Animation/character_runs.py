from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here

frame = 0
other_frame = 0

def character_run():
    global frame
    global other_frame
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(
        frame * 100, other_frame * 100, # left, bottom
        100, 100, # width, height 텍스처 상 크기
        x, 90, # destination x, y
        # 200, 200 # width, height 출력할 크기(확대)
    )
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)


while True:
    for x in range(750, 0, -5):
        character_run()
    other_frame = (other_frame + 1) % 4

    for x in range(0, 750, 5):
        character_run()
    other_frame = (other_frame + 1) % 4

close_canvas()