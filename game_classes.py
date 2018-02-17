import pygame
import random
import math
from actions import *

class Zombie(pygame.sprite.Sprite): #Basic zombie
    def __init__(self,color,gameWidth,gameHeight,player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(color)
        self.strength = 10
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, gameWidth)
        self.rect.y = random.randrange(0, gameHeight)
        self.speed = 2.3
        self.cd = 0
        self.cdMax = 30
    def move(self,player):
        xdiff = self.rect.x - player.rect.x
        ydiff = self.rect.y - player.rect.y
        if(xdiff < -8) or (xdiff > 8) or (ydiff < -8) or (ydiff > 8):
            mvmt = calcMove(self.speed, self.rect.x, self.rect.y, player.rect.x, player.rect.y)
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




class bigZombie(Zombie):
    def __init__(self,color,gameWidth,gameHeight,player):
        super().__init__(color,gameWidth,gameHeight,player)
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.speed = 1.5
    def attack(self):
        print("You got bitch slapped!")
        self.cd = self.cdMax