import random
import math
import cmath


from pico2d import *

class Enemy:
    image = None
    hit_sound = None
    PI = 3.141592654


    def __init__(self):
        #self.x, self.y = random.randint(200, 700), 500
        self.x, self.y = -50, 500
        self.startX = random.randint(200, 700)
        self.startY = 500
        self.on = 0
        self.HP = 2
        self.operate = 1
        self.ndt = 0.1
        self.ndtPlus = 0.1
        self.scunt = 0
        self.bullet = [Bullet() for i in range(108)]

            #ppself.hit_sound.play()
        if Enemy.image == None:
            Enemy.image = load_image('twitter.png')

    def update(self, frame_time):
        self.x = self.startX
        self.y = self.startY
        self.on = 1
        if self.startX > 400:
            self.startX += frame_time * 60
        if self.startX <= 400:
            self.startX -= frame_time * 60
        self.ndtPlus += frame_time
        self.ndt = round(self.ndtPlus, 1)

        #print(self.ndt)
        #if(0>= )
        if self.operate == 1:
            self.fire()
        if self.HP <= 0 or self.ndt >= 12:
            self.operate = 0
            self.on = 0
        for i in range(108):
            if self.bullet[i].on:
                self.bullet[i].x += math.cos(self.bullet[i].angle) * self.bullet[i].speed * frame_time * 50
                self.bullet[i].y += math.sin(self.bullet[i].angle) * self.bullet[i].speed * frame_time * 50
            if self.bullet[i].x < 0 or self.bullet[i].x > 800 or self.bullet[i].y < 0 or self.bullet[i].y > 600:
                #self.bullet[i].on = 0
                self.bullet[i].x = - 50
                self.bullet[i].y = - 50
        if self.operate == 0:
            self.x = 0
            self.y = -50
            #self.index += 1






        #self.x, self.y = 400,300


    def draw(self):
        self.image.draw(self.x, self.y, 75, 75)
        for i in range(108):
            if (self.bullet[i].on):
                self.bullet[i].image.draw(self.bullet[i].x, self.bullet[i].y, 20, 20)

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def fire(self):
        if self.ndt % 1 == 0:
            for i in range(36):
                if self.bullet[i].on == 1:
                    continue
                self.bullet[i].on = 1
                self.bullet[i].angle = (math.pi * 3 / 2) + i * 36
                self.bullet[i].x = math.cos(self.bullet[i].angle) + self.x
                self.bullet[i].y = -math.sin(self.bullet[i].angle)  + self.y

        if self.ndt % 2 == 0:
            for i in range(36, 72):
                if self.bullet[i].on == 1:
                    continue
                self.bullet[i].on = 1
                self.bullet[i].angle = (math.pi * 3 / 2) + i * 36
                self.bullet[i].x = math.cos(self.bullet[i].angle) + self.x
                self.bullet[i].y = -math.sin(self.bullet[i].angle) + self.y

        if self.ndt % 3 == 0:
            for i in range(72, 108):
                if self.bullet[i].on == 1:
                    continue
                self.bullet[i].on = 1
                self.bullet[i].angle = (math.pi * 3 / 2) + i * 36
                self.bullet[i].x = math.cos(self.bullet[i].angle) + self.x
                self.bullet[i].y = -math.sin(self.bullet[i].angle) + self.y

    def __delete__(self):
        del(self)

    def hit(self):
        self.hit_sound.play()


class Bullet:
    image = None

    def __init__(self):
        self.on = 0
        self.x, self.y = -50, -50
        self.angle = 0
        self.radius = 0
        self.speed = 3
        if Bullet.image == None:
            Bullet.image = load_image('bullet.png')

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
