from pico2d import *


open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('sonic_3_custom_sprites_by_facundogomez_dawphra.png')



def handle_events():
    global running, hordir, verdir, hornum, upframe, downframe, idleframe

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                hordir+=1
            elif event.key == SDLK_LEFT:
                hordir-=1
            if event.key == SDLK_UP:
                verdir+=1
            elif event.key == SDLK_DOWN:
                verdir-=1
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                hordir -=1
            elif event.key == SDLK_LEFT:
                hordir+=1
            if event.key == SDLK_UP:
                verdir -=1

            elif event.key == SDLK_DOWN:
                verdir+=1
            hornum=0
            upframe =0
            downframe = 0
            idleframe = 0

running = True
x = 800 // 2
y = 600//2
upframe = 0
downframe = 0
idleframe = 0
hor1frame = [0,50,97,149,200,245, 295, 350, 394]
hordir = 0
verdir = 0
hornum=0


while running:
    clear_canvas()
    grass.draw(400,300)
    if hordir == 1:
        character.clip_draw(hor1frame[hornum],350,hor1frame[hornum+1] - hor1frame[hornum],50,x,y)
        hornum = (hornum + 1) % 8
    elif hordir ==-1:
        character.clip_composite_draw(hor1frame[hornum], 350, hor1frame[hornum + 1] - hor1frame[hornum], 50,0,'h', x, y,50,50)
        hornum = (hornum + 1) % 8
    elif verdir == 1:
        character.clip_draw(upframe * 40, 85, 40, 50, x, y)
        upframe = (upframe + 1) % 10
    elif verdir == -1:
        character.clip_draw(downframe * 47, 210, 47, 60, x, y)
        downframe = (downframe + 1) % 8
    elif hordir == 0 and verdir ==0:
        character.clip_draw(idleframe*46, 595, 46, 50, x, y)
        idleframe = (idleframe+1)%15
    update_canvas()
    handle_events()
    if 790 >= x:
        x += hordir * 5
    else:
        x = 790
    if 10 <= x:
        x += hordir * 5
    else:
        x = 10
    if 590 >= y:
        y += verdir * 5
    else:
        y=590
    if 10 <= y:
        y += verdir * 5
    else:
        y=10
    delay(0.05)


close_canvas()

