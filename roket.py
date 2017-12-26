from pico2d import*


class Roket:
    missiles = None
    hit_sound = None
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 2
        #self.image = load_image('run_animation.png')
        self.heart = 5
        self.image = load_image('rocket.png')
        self.heart_image = load_image('heart.png')
        self.dir = 1
        self.speed = 6
        self.LEFT_DOWN = 0
        self.RIGHT_DOWN = 0
        self.UP_DOWN = 0
        self.DOWN_DOWN = 0
        self.fire_image = load_image('ball21x21.png')
        self.missiles = [Missile() for i in range(15)]
        self.index = 0
        if Roket.hit_sound == None:
            Roket.hit_sound = load_wav('Slap_with_Glove2.wav')
            Roket.hit_sound.set_volume(32)

    def update(self, frame_time):
        if self.LEFT_DOWN == 1 and self.x > 0:
            self.x -= self.speed * frame_time * 50
        if self.RIGHT_DOWN == 1and self.x < 800:
            self.x += self.speed * frame_time * 50
        if self.UP_DOWN == 1 and self.y < 600:
            self.y += self.speed * frame_time * 50
        if self.DOWN_DOWN == 1 and self.y > 0:
            self.y -= self.speed * frame_time * 50
        if self.LEFT_DOWN == 1:
            self.frame = 0
        if self.RIGHT_DOWN == 1:
            self.frame = 4
        if self.LEFT_DOWN == 0 and self.RIGHT_DOWN ==0 :
            self.frame = 2

        for i in range(15):
            if self.missiles[i].on:
                self.missiles[i].y += frame_time * 500
            if self.missiles[i].y > 600:
                self.missiles[i].on = 0
            if self.missiles[i].on == 0:
                self.missiles[i].x, self.missiles[i].y = -50, -50



    def draw(self):
        self.image.clip_draw(self.frame * 38, 0, 38, 38, self.x, self.y)
        for i in range(15):
            if self.missiles[i].on:
                self.missiles[i].image.draw(self.missiles[i].x, self.missiles[i].y)

        for i in range(self.heart):
            self.heart_image.draw(20 * i + 20 , 20, 20, 20)


    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self,event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.LEFT_DOWN = 1

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.RIGHT_DOWN = 1

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.LEFT_DOWN = 0

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.RIGHT_DOWN = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.UP_DOWN = 1

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.DOWN_DOWN = 1

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            self.UP_DOWN = 0

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.DOWN_DOWN = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            self.fire()

    def fire(self):
        self.missiles[self.index].x, self.missiles[self.index].y = self.x, self.y
        self.missiles[self.index].on = 1
        self.index += 1
        if self.index > 14:
            self.index = 0

    def bomb(self):
        pass

    def hit_enemy(self, enemy):
        self.hit_sound.play()

    def hit_boss(self, boss):
        self.hit_sound.play()
class Missile(Roket):
    image = None

    def __init__(self):
        self.on = 0
        self.x, self.y = -50, -50
        self.fall_speed = 5
        if Missile.image == None:
            Missile.image = load_image('ball21x21.png')

    def update(self):
        #self.y -= frame_time * self.fall_speed
        #self.y += self.fall_speed
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def fire(self):
        #self.x, self.y = Roket.x, Roket.y
        pass