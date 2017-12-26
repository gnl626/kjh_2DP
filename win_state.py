import game_framework
import main_state
import title_state
import enemy
import roket
from pico2d import*

name = "WinState"
image = None
counter = 0

def enter():
    global image
    image = load_image('lol_victory.png')


def exit():
    global image
    del(image)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(title_state)



def draw(frame_time):

    clear_canvas()
    main_state.draw_main_scene()
    image.draw(400, 500)

    update_canvas()






def update(frame_time):
    global counter
    counter = (counter + 1) % 100


def pause():
    pass


def resume():
    pass