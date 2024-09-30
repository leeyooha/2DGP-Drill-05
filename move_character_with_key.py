from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('oak.png')

left, right, up, down = False, False, False, False

running = True
x, y = 800 // 2, 90
frame = 0

def handle_events():
    global running
    global left, right, up, down
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                left = True
            elif event.key == SDLK_RIGHT:
                right = True
            elif event.key == SDLK_UP:
                up = True
            elif event.key == SDLK_DOWN:
                down = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                left = False
            elif event.key == SDLK_RIGHT:
                right = False
            elif event.key == SDLK_UP:
                up = False
            elif event.key == SDLK_DOWN:
                down = False

# 메인 루프
while running:
    handle_events()  # 이벤트 처리
    clear_canvas()
    grass.draw(400, 300)  # 배경 그리기
    if left:
        x -= 5
        character.clip_draw(frame * 175, 2 * 245, 170, 245, x, y)  # 왼쪽 이동 애니메이션
    elif right:
        x += 5
        character.clip_draw(frame * 175, 1 * 245, 170, 245, x, y)  # 오른쪽 이동 애니메이션
    elif up:
        y += 5
        character.clip_draw(frame * 175, 0 * 245, 170, 245, x, y)  # 위로 이동 애니메이션
    elif down:
        y -= 5
        character.clip_draw(frame * 175, 3 * 245, 170, 245, x, y)  # 아래로 이동 애니메이션
    else:
        character.clip_draw(frame * 175, 3 * 245, 170, 245, x, y)  # 입력이 없을 때 기본 애니메이션
    update_canvas()
    frame = (frame + 1) % 4  # 4개의 프레임 순환
    delay(0.05)

close_canvas()
