from pico2d import *

import game_framework
from ball import Ball

from boy import FreeBoy as Boy # import Boy class from boy.py

from background import  FixedTileBackground as Background

from TileMap import  load_tile_map

name = "scroll_state"

boy = None
background = None
balls = None

def create_world():
    global boy, background, balls
    balls = [Ball() for i in range(2)]
    boy = Boy()
    background = Background()
    balls[0].x = 190.666666666667
    balls[0].y = 600 - 97.3333333333333
    balls[1].x = 264
    balls[1].y = 600 - 216

    # fill here
    background.set_center_object(boy)
    boy.set_background(background)


def destroy_world():
    global boy, background
    del(boy)
    del(background)


def enter():
    open_canvas(800, 600, sync=True)
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)



def update(frame_time):
    boy.update(frame_time)
    background.update(frame_time)



def draw(frame_time):
    clear_canvas()
    background.draw()
    boy.draw()
    for i in range(2):
        balls[i].draw()
    update_canvas()






