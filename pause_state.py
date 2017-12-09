import game_framework
import main_state
import enemy
import roket
from pico2d import*

name = "PasueState"
image = None
counter = 0

def enter():
    global image
    image = load_image('you_died.jpg')


def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()



def draw():

    clear_canvas()
    main_state.draw_main_scene()
    if counter < 50:
        image.draw(400, 300)
    update_canvas()






def update():
    global counter
    counter = (counter + 1) % 100


def pause():
    pass


def resume():
    pass