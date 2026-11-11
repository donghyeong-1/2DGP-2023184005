from pico2d import load_image, get_time, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from transitions import Machine


class Idle:
    def __init__(self, boy):
        self.boy = boy

    def enter(self):
        self.boy.frame = 0
        self.start_time = get_time()

    def exit(self):
        pass

    def do(self):
        self.boy.frame = (self.boy.frame + 1) % 8
        if self.boy.dir != 0:  # 방향키가 눌린 채로 IDLE에 들어온 경우
            self.boy.arrow_down()
        elif get_time() - self.start_time > 5:
            self.boy.time_out()

    def draw(self):
        if self.boy.face_dir == 1:
            self.boy.image.clip_draw(self.boy.frame * 100, 300, 100, 100, self.boy.x, self.boy.y)
        else:
            self.boy.image.clip_draw(self.boy.frame * 100, 200, 100, 100, self.boy.x, self.boy.y)


class Run:
    SPEED = 5
    HALF_W = 25  # 화면 밖으로 나가지 않게 하는 여유 (스프라이트 절반 폭)

    def __init__(self, boy):
        self.boy = boy

    def enter(self):
        self.boy.frame = 0

    def exit(self):
        pass

    def do(self):
        self.boy.frame = (self.boy.frame + 1) % 8
        if self.boy.dir != 0:
            self.boy.face_dir = self.boy.dir
        self.boy.x += self.boy.dir * Run.SPEED
        self.boy.x = max(Run.HALF_W, min(800 - Run.HALF_W, self.boy.x))

    def draw(self):
        if self.boy.face_dir == 1:
            self.boy.image.clip_draw(self.boy.frame * 100, 100, 100, 100, self.boy.x, self.boy.y)
        else:
            self.boy.image.clip_draw(self.boy.frame * 100, 0, 100, 100, self.boy.x, self.boy.y)


class Sleep:
    def __init__(self, boy):
        self.boy = boy

    def enter(self):
        self.boy.frame = 0

    def exit(self):
        pass

    def do(self):
        self.boy.frame = (self.boy.frame + 1) % 8

    def draw(self):
        if self.boy.face_dir == 1:
            self.boy.image.clip_composite_draw(
                self.boy.frame * 100, 300, 100, 100,
                3.141592 / 2, '',
                self.boy.x - 25, self.boy.y - 25, 100, 100
            )
        else:
            self.boy.image.clip_composite_draw(
                self.boy.frame * 100, 200, 100, 100,
                -3.141592 / 2, '',
                self.boy.x + 25, self.boy.y - 25, 100, 100
            )


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.left_held = False
        self.right_held = False
        self.image = load_image('animation_sheet.png')

        # 상태 이름 -> 상태 객체
        self.IDLE = Idle(self)
        self.RUN = Run(self)
        self.SLEEP = Sleep(self)
        self.states = {'IDLE': self.IDLE, 'RUN': self.RUN, 'SLEEP': self.SLEEP}

        # transitions 상태머신 : Boy 객체에 self.state 속성이 생긴다
        self.machine = Machine(
            model=self,
            states=[
                {'name': 'IDLE', 'on_enter': self.IDLE.enter, 'on_exit': self.IDLE.exit},
                {'name': 'RUN', 'on_enter': self.RUN.enter, 'on_exit': self.RUN.exit},
                {'name': 'SLEEP', 'on_enter': self.SLEEP.enter, 'on_exit': self.SLEEP.exit},
            ],
            transitions=[
                {'trigger': 'arrow_down', 'source': ['IDLE', 'SLEEP'], 'dest': 'RUN'},
                {'trigger': 'arrow_up', 'source': 'RUN', 'dest': 'IDLE', 'conditions': 'no_arrow_held'},
                {'trigger': 'time_out', 'source': 'IDLE', 'dest': 'SLEEP'},
                {'trigger': 'space_down', 'source': 'SLEEP', 'dest': 'IDLE'},
            ],
            initial='IDLE',
            ignore_invalid_triggers=True,
        )
        self.IDLE.enter()  # transitions는 초기 상태의 on_enter를 호출하지 않으므로 직접 호출

    @property
    def dir(self):
        return int(self.right_held) - int(self.left_held)

    def no_arrow_held(self):
        return self.dir == 0

    def update(self):
        self.states[self.state].do()

    def draw(self):
        self.states[self.state].draw()

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            self.space_down()
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP) and event.key in (SDLK_LEFT, SDLK_RIGHT):
            pressed = event.type == SDL_KEYDOWN
            if event.key == SDLK_LEFT:
                self.left_held = pressed
            else:
                self.right_held = pressed
            if pressed:
                self.arrow_down()
            else:
                self.arrow_up()
