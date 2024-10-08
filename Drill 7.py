import random
from pico2d import *

class Grass:
    # 생성자 함수: 객체의 초기 상태를 설정, 메모리 할당
    def __init__(self):
        # 모양 없는 납작한 붕어빵의 초기모습 결정
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)

class Big_ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global big_balls

    running = True
    big_balls = [Big_ball() for i in range(10)]
    pass

def render_world():
    clear_canvas()
    grass.draw()

    for ball in big_balls:
        ball.update()
    pass

def update_world():
    pass

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()