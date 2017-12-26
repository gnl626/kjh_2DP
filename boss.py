import random
import math
import cmath


from pico2d import *

class Boss:
    image = None
    bgm = None
    PI = 3.141592654

    def __init__(self):
        self.x, self.y = 400, 800
        self.on = 0
        self.HP = 280
        self.operate = 1
        self.ndt = 0
        self.ndtPlus = 0
        self.bullet = [Bullet() for i in range(324)]
        if Boss.image == None:
            Boss.image = load_image('Boss.png')

    def update(self, frame_time):
        if self.ndtPlus < 1:
            for i in range(108):
                self.bullet[i].x = random.randint(0, 800)
                self.bullet[i].y = random.randint(600, 1800)
                self.bullet[i].on = 1
            for i in range(108, 216):
                self.bullet[i].angle = (math.pi * 3 / 2) + i * 36
                self.bullet[i].x = math.cos(self.bullet[i].angle) + self.x
                self.bullet[i].y = -math.sin(self.bullet[i].angle) + self.y - 200
                self.bullet[i].on = 0
            for i in range(216, 324):
                self.bullet[i].angle = (math.pi * 3 / 2) + i * 36
                self.bullet[i].x = math.cos(self.bullet[i].angle) + self.x
                self.bullet[i].y = -math.sin(self.bullet[i].angle) + self.y - 200
                self.bullet[i].on = 0
        self.ndtPlus += frame_time
        self.ndt = round(self.ndtPlus, 1)
        #print(self.ndt)
        if self.y > 600:
            self.y -= frame_time * 200

        if self.ndt < 8:
            self.patton1_rain(frame_time)
        if self.ndt > 6 and self.ndt < 12:
            self.patton2_round(frame_time)
        if self.ndt > 12 and self.ndt < 18:
            self.patton3_spin(frame_time)
        if self.ndt > 18:
            self.ndtPlus = 0

    def draw(self):
        #self.bullet[0].image.draw(400 , 300, 20, 20)
        for i in range(324):
            if (self.bullet[i].on) :
                self.bullet[i].image.draw(self.bullet[i].x, self.bullet[i].y, 20, 20)

        self.image.draw(self.x, self.y, 800, 600)

    def get_bb(self):
        return self.x - 400, self.y - 100, self.x + 400, self.y + 100

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def patton1_rain(self, frame_time):
        for i in range(108):
            self.bullet[i].y -= frame_time * 350
    def patton2_round(self, frame_time):
        if self.ndt % 1 == 0:
            for i in range(108, 144):
                self.bullet[i].on = 1
        if self.ndt % 2 == 0:
            for i in range(144, 180):
                self.bullet[i].on = 1
        if self.ndt % 3 == 0:
            for i in range(180, 216):
                self.bullet[i].on = 1
        for i in range(108, 216):
            if self.bullet[i].on:
                self.bullet[i].x += math.cos(self.bullet[i].angle) * frame_time * 200
                self.bullet[i].y += math.sin(self.bullet[i].angle) * frame_time * 200

    def patton3_spin(self, frame_time):
        if self.ndt % 1 == 0:
            for i in range(216, 252):
                self.bullet[i].on = 1
        if self.ndt % 2 == 0:
            for i in range(252, 288):
                self.bullet[i].on = 1
        if self.ndt % 3 == 0:
            for i in range(288, 324):
                self.bullet[i].on = 1
        for i in range(216, 324):
            if self.bullet[i].on:
                self.bullet[i].x += math.cos(self.bullet[i].angle) * frame_time * 300
                self.bullet[i].y += math.sin(self.bullet[i].angle) * frame_time * 300












class Bullet:
    image = None

    def __init__(self):
        self.on = 0
        self.x, self.y = -50, -50
        self.angle = 0
        self.radius = 0
        self.speed = 3
        if Bullet.image == None:
            Bullet.image = load_image('bullet2.png')

    def update(self, frame_time):
        # self.y -= frame_time * self.fall_speed
        # self.y += self.fall_speed
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def fire(self):
        # self.x, self.y = Roket.x, Roket.y
        pass