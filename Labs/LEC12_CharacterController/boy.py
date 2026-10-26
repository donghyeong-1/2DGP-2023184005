from pico2d import load_image
from transitions import Machine


class Idle:
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
            self.boy.image.clip_draw(self.boy.frame * 100, 300, 100, 100, self.boy.x, self.boy.y)
        else:
            self.boy.image.clip_draw(self.boy.frame * 100, 200, 100, 100, self.boy.x, self.boy.y)


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')

        # 상태 이름 -> 상태 객체
        self.IDLE = Idle(self)
        self.states = {'IDLE': self.IDLE}

        # transitions 상태머신 : Boy 객체에 self.state 속성이 생긴다
        self.machine = Machine(
            model=self,
            states=[{'name': 'IDLE', 'on_enter': self.IDLE.enter, 'on_exit': self.IDLE.exit}],
            initial='IDLE',
        )
        self.IDLE.enter()  # transitions는 초기 상태의 on_enter를 호출하지 않으므로 직접 호출

    def update(self):
        self.states[self.state].do()

    def draw(self):
        self.states[self.state].draw()
