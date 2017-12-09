import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
from roket import Roket
from enemy import Enemy

name = "MainState"

grass = None
font = None
roket = None
enemy = None
play = 1
num = 0
numcount = 0
PAUSED = None
boyX = 0
boyY = 90
LEFT_DOWN = 0
RIGHT_DOWN = 0
UP_DOWN = 0
DOWN_DOWN = 0
ndt = 0

class Grass:
    def __init__(self):
        self.image = load_image('bluesky.bmp')
        self.x, self.y = 400, 300
        self.x2, self.y2 = 400, 900

    def update(self, frame_time
               ):
        self.y -= 1
        if self.y < -300:
            self.y = 900
        self.y2 -= 1
        if self.y2 < -300:
            self.y2 = 900


    def draw(self):
        self.image.draw(self.x, self.y, 800, 610)
        self.image.draw(self.x, self.y2, 800, 610)
        #self.image.rotate_draw(6, 400, 300, 800, 600)


def enter():
    global  grass, PAUSED, roket, enemy
    grass = Grass()
    roket = Roket()
    enemy = Enemy()
    PAUSED = load_image("you_died.jpg")


def exit():
    global grass, roket, enemy
    del(grass)
    del(roket)
    del(enemy)



def pause():
    #game_framework.push_state(pause_state)
    pass
def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            roket.handle_event(event)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True



def update(frame_time):
    roket.update(frame_time)
    grass.update(frame_time)
    enemy.update(frame_time)
    for i in range(108):
        if collide(enemy.bullet[i], roket):
            print("collide")
            #print(enemy.ndt)
            #game_framework.push_state(pause_state)
    for i in range(15):
        if collide(roket.missiles[i], enemy):
            roket.missiles[i].on = 0
    delay(0.01)


def draw(frame_time):
    clear_canvas()
    draw_main_scene()
    update_canvas()

def draw_main_scene():
    grass.draw()
    roket.draw()
    enemy.draw()
    roket.draw_bb()
    enemy.draw_bb()
    for i in range(15):
        roket.missiles[i].draw_bb()
    for i in range(108):
        enemy.bullet[i].draw_bb()




