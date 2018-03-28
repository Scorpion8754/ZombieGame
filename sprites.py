import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((24, 24))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 4

    def move(self, xdir, ydir):
        xdir *= self.speed
        ydir *= self.speed
        if not self.collide_with_walls(xdir, ydir):
            self.x += xdir
            self.y += ydir

    def collide_with_walls(self, dx=0, dy=0):
        collide = pg.sprite.spritecollide(self, self.game.walls, False)
        if collide:
            return True
        return False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Zombie(pg.sprite.Sprite): #Basic zombie
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((24, 24))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 2.3
        self.cd = 0
        self.cdMax = 30
    def move(self,target):
        xdiff = self.rect.x - target.rect.x
        ydiff = self.rect.y - target.rect.y
        if(xdiff < -8) or (xdiff > 8) or (ydiff < -8) or (ydiff > 8):
            mvmt = calcMove(self.speed, self.rect.x, self.rect.y, target.rect.x, target.rect.y)
            if self.cd < 0:
                self.rect.x = mvmt[0]
                self.rect.y = mvmt[1]
                if(xdiff >= -15) and (xdiff <= 15) and (ydiff >= -15) and (ydiff <= 15):
                    self.attack()
    def attack(self):
        print("You got slapped!")
        self.cd = self.cdMax
    def update(self):
        self.cd -= 1
        self.move(self.game.player)