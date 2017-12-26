import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import win_state
from roket import Roket
from enemy import Enemy
from boss import Boss

name = "MainState"

grass = None
font = None
roket = None
enemy = None
enemys = None
boss = None
play = 1
num = 0
count = 0
immortal = 0
immortalCount = 0
numcount = 0
PAUSED = None
boyX = 0
boyY = 90
LEFT_DOWN = 0
RIGHT_DOWN = 0
UP_DOWN = 0
DOWN_DOWN = 0
ndtPlus = 0
ndt = 0
hit_sound = None

class Grass:
    def __init__(self):
        self.image = load_image('bluesky.bmp')
        self.x, self.y = 400, 300
        self.x2, self.y2 = 400, 900
        #self.bgm = load_music('Fight_or_Flight.mp3')
        #self.bgm.set_volume(64)
        #self.bgm.repeat_play()

    def update(self, frame_time):
        self.y -= 5
        if self.y < -300:
            self.y = 900
        self.y2 -= 5
        if self.y2 < -300:
            self.y2 = 900


    def draw(self):
        self.image.draw(self.x, self.y, 800, 610)
        self.image.draw(self.x, self.y2, 800, 610)
        #self.image.rotate_draw(6, 400, 300, 800, 600)


def enter():
    global  grass, PAUSED, roket, enemy, enemys, boss, hit_sound
    grass = Grass()
    roket = Roket()
    enemys = [Enemy() for i in range (8)]
    boss = Boss()
    PAUSED = load_image("you_died.jpg")
    hit_sound = load_wav('Slap_with_Glove2.wav')
    hit_sound.set_volume(32)


def exit():
    global grass, roket, enemy, boss, enemys
    del(grass)
    del(roket)
    del(enemy)
    del(boss)
    del(enemys)



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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            game_framework.push_state(win_state)
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

#ndtPlus = 23

def update(frame_time):
    global enemy, count, immortal, ndt, ndtPlus, immortalCount
    count += 1
    ndtPlus += frame_time
    ndt = round(ndtPlus, 1)
    #print(ndt)
    roket.update(frame_time)
    grass.update(frame_time)
    #enemy.update(frame_time)
    if  ndt > 1 and ndt < 12:
        enemys[0].update(frame_time)
        enemys[1].update(frame_time)
        if collide(enemys[0], enemys[1]):
            enemys[0].startX = enemys[0].startX - 100
    elif ndt > 12 and ndt < 22:
        enemys[2].update(frame_time)
        enemys[3].update(frame_time)
        if collide(enemys[2], enemys[3]):
            enemys[2].startX = enemys[2].startX - 100
    elif ndt > 24 and ndt < 36:
        enemys[4].update(frame_time)
        enemys[5].update(frame_time)
        if collide(enemys[4], enemys[5]):
            enemys[4].startX = enemys[4].startX - 100
    elif ndt > 36 and ndt < 48:
        enemys[6].update(frame_time)
        enemys[7].update(frame_time)
        if collide(enemys[6], enemys[7]):
            enemys[6].startX = enemys[6].startX - 100
    elif ndt > 48:
        boss.update(frame_time)
        #enemys[8].update(frame_time)
    #for i in range(8):
        #enemys[i].update(frame_time)
    for i in range(108):
        for j in range(8):
            if collide(enemys[j].bullet[i], roket) and immortal == 0:
                print("collide")
                roket.heart -= 1
                immortal = 1
                #game_framework.push_state(pause_state)
    for i in range(324):
        if collide(boss.bullet[i], roket) and immortal == 0:
            print("collide")
            roket.heart -= 1
            immortal = 1

    if immortal:
        immortalCount += frame_time
    if immortalCount > 2:
        immortal = 0
        immortalCount = 0

    if roket.heart == -1:
        roket.heart = 5
        #game_framework.push_state(pause_state)

    for i in range(15):
        for j in range(8):
            if collide(roket.missiles[i], enemys[j]) and enemys[j].on:
                roket.missiles[i].on = 0
                enemys[j].HP -= 1
                roket.hit_enemy(enemys[j])
                #enemys[j].hit()
        if collide(roket.missiles[i], boss) and ndt > 48:
            roket.missiles[i].on = 0
            boss.HP -= 1
            roket.hit_enemy(boss)

    if boss.HP == 0:
        game_framework.push_state(win_state)
    print(boss.HP)
    print(ndt)




def draw(frame_time):
    clear_canvas()
    draw_main_scene()
    update_canvas()

def draw_main_scene():
    global ndt, immortal
    grass.draw()
    #boss.draw_bb()
    if immortal == 0:
        roket.draw()
    if immortal and count % 2 == 0:
        roket.draw()
    #enemy.draw()
    if ndt < 12:
        enemys[0].draw()
        enemys[1].draw()
    elif ndt > 12 and ndt < 24:
        enemys[2].draw()
        enemys[3].draw()
    elif ndt > 24 and ndt < 36:
        enemys[4].draw()
        enemys[5].draw()
    elif ndt > 36 and ndt < 48:
        enemys[6].draw()
        enemys[7].draw()
    elif ndt > 48:
        boss.draw()





