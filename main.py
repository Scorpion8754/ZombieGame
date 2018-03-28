import pygame
import sys
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(1)
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self, 10, 10)
        for x in range(10, 20):
            Wall(self, x, 5)
            pass
        self.enemies.add(Zombie(self, 10, 10))


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            activeKey = pygame.key.get_pressed()
            if activeKey[pygame.K_ESCAPE]:
                self.quit()
            if activeKey[pygame.K_a]:
                self.player.move(-1, 0)
            if activeKey[pygame.K_d]:
                self.player.move(1, 0)
            if activeKey[pygame.K_w]:
                self.player.move(0, -1)
            if activeKey[pygame.K_s]:
                self.player.move(0, 1)
            if activeKey[pygame.K_0]:
                self.enemies.add(Zombie(self, random.randrange(0, WIDTH), random.randrange(0, HEIGHT)))
    def quit(self):
        pg.quit()
        sys.exit()


    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
g.show_go_screen()