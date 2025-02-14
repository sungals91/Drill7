from pico2d import *
import random

# Game object class here

class Grass:
    # 생성자 함수: 객체의 초기 상태를 설정, 메모리 할당
    def __init__(self):
        # 모양 없는 납작한 붕어빵의 초기모습 결정
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,400), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        pass
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Big_ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')
    def update(self):
        speed = random.randint(2,10)
        self.y -= speed
        if self.y <= 80:
            self.y = 80
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
        pass

class Small_ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 599
        self.image = load_image('ball21x21.png')
    def update(self):
        speed = random.randint(2,10)
        self.y -= speed
        if self.y <= 80:
            self.y = 80
        pass
    def draw(self):
        self.image.draw(self.x, self.y)


def reset_world():
    global running
    global grass
    #global boy
    global team
    global big
    global small

    running = True
    grass = Grass() # 잔디를 찍어낸다
    #boy = Boy()
    team = [Boy() for i in range(10)]
    big = [Big_ball() for i in range (10)]
    small = [Small_ball() for i in range(10)]

def update_world():
    grass.update() # Grass 상태를 업데이트
    #boy.update()
    for boy in team:
        boy.update()
    for ball in big:
        ball.update()
    for ball in small:
        ball.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    #boy.draw()
    for boy in team:
        boy.draw()
    for ball in big:
        ball.draw()
    for ball in small:
        ball.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

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
