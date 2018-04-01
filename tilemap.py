import pygame as pg
from settings import *
vec = pg.math.Vector2

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, 450, 450)
        self.width = width
        self.height = height
        self.StartHeight = height
        self.StartWidth = width

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def mouseAdjustment(self, mouse):
        return vec(mouse) + vec(-self.camera.left, -self.camera.top)

    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y =  -target.rect.centery + int(HEIGHT / 2)

        #limit scrolling to map size
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x) #right
        y = max(-(self.height - HEIGHT), y) #bottom
        self.camera = pg.Rect(x, y, self.width, self.height)


    def AdjustZoom(self, input):
        if input == 'reset':
            self.height = self.startHeight
            self.width = self.startWidth
        else:
            self.camera = pg.Rect(0, 0, (self.width+200), (self.height+200))