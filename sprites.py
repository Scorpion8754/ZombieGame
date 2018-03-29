import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((24, 24))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 200

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx += -self.speed
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx += self.speed
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy += self.speed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy += -self.speed
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vx = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')


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
        self.vx, self.vy = 0, 0
        self.speed = 2.3
        self.cd = 0
        self.cdMax = 30
    def move(self):
        target = self.game.player
        xdiff = self.rect.x - target.rect.x
        ydiff = self.rect.y - target.rect.y
        if(xdiff < -8) or (xdiff > 8) or (ydiff < -8) or (ydiff > 8):
            if self.cd < 0:
                mvmt = calcMove(self.speed, self.rect.x, self.rect.y, target.rect.x, target.rect.y)
                self.vx = mvmt[0]
                self.vy = mvmt[1]
                if(xdiff >= -15) and (xdiff <= 15) and (ydiff >= -15) and (ydiff <= 15):
                    self.attack()
    def attack(self):
        print("You got slapped!")
        self.cd = self.cdMax
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx < 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx > 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vx = 0
                self.rect.y = self.y
    def update(self):
        self.cd -= 1
        self.move()
        self.x -= self.vx
        self.y += self.vy
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')