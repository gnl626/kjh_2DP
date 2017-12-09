from pico2d import*


class Roket:
    missiles = None
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 2
        #self.image = load_image('run_animation.png')
        self.image = load_image('rocket.png')
        self.dir = 1
        self.speed = 5
        self.LEFT_DOWN = 0
        self.RIGHT_DOWN = 0
        self.UP_DOWN = 0
        self.DOWN_DOWN = 0
        self.fire_image = load_image('ball21x21.png')
        self.missiles = [Missile() for i in range(15)]
        self.index = 0

    def update(self):
        if self.LEFT_DOWN == 1 and self.x > 0:
            self.x -= self.speed
        if self.RIGHT_DOWN == 1and self.x < 800:
            self.x += self.speed
        if self.UP_DOWN == 1 and self.y < 600:
            self.y += self.speed
        if self.DOWN_DOWN == 1 and self.y > 0:
            self.y -= self.speed
        for i in range(15):
            if self.missiles[i].on:
                self.missiles[i].y += self.speed * 2
            else:
                self.missiles[i].x, self.missiles[i].x = -50, -50



    def draw(self):
        self.image.clip_draw(self.frame * 38, 0, 38, 38, self.x, self.y)
        for i in range(15):
            if self.missiles[i].on:
                self.missiles[i].image.draw(self.missiles[i].x, self.missiles[i].y)

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