import pygame
import random
import math


pygame.init()
gameWidth = 1280
gameHeight = 720
gameWindow = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption("ZOMBIE GAME")
clock = pygame.time.Clock()



#Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (153, 153, 0)
#Globals
bullets = []
zombies = []


def calcMove(speed, fromx, fromy, tox, toy):  # I'm going this fast, want to get from(x,y) to(x,y)
    run = fromx - tox
    rise = toy - fromy
    length = math.sqrt((rise * rise) + (run * run))
    unitx = run / length
    unity = rise / length
    fromx -= int(unitx * speed)
    fromy += int(unity * speed)
    return (fromx, fromy)




class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(red)
        self.strength = 10
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, gameWidth)
        self.rect.y = random.randrange(0, gameHeight)
        self.speed = 2.3
        self.cd = 0
        self.cdMax = 30
    def move(self):
        xdiff = self.rect.x - player.rect.x
        ydiff = self.rect.y - player.rect.y
        if(xdiff < -8) or (xdiff > 8):
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
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(yellow)
        self.speed = 1.5
    def attack(self):
        print("You got bitch slapped!")
        self.cd = self.cdMax

class playerActive():
    def __init__(self):
        self.image = pygame.Surface((15, 15))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 4
        self.ammo = 100
        self.cd = 10
        self.cdMax = 10
        self.isHealing = False
    def move(self, xdir, ydir):
        self.rect.x += xdir*self.speed
        self.rect.y += ydir*self.speed
    def shoot(self):
        if self.cd <= 0 and self.ammo:
            self.cd = self.cdMax
            bullet = self.ammo.pop()
            bullet.rect.x = self.rect.x + self.rect.width/2 - bullet.rect.width/2
            bullet.rect.y = self.rect.y + self.rect.height/2 - bullet.rect.height/2
            bullet.getTarg()
            bullets.append(bullet)
    def update(self):
        self.cd -= 1



all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group
player = playerActive()
for i in range(2):
    z = Zombie()
    all_sprites.add(z)
    mobs.add(z)
zombies.append(bigZombie())


#Game Start
gameActive = True
fps = 60
while gameActive:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameActive = False

    activeKey = pygame.key.get_pressed()
    if activeKey[pygame.K_d]:
        player.move(1, 0)
    if activeKey[pygame.K_a]:
        player.move(-1, 0)
    if activeKey[pygame.K_w]:
        player.move(0, -1)
    if activeKey[pygame.K_s]:
        player.move(0, 1)
    if activeKey[pygame.K_0]:
        zombies.append(Zombie())

    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        #player.shoot()
        pass

    #Do Math Stuff
    for obj in bullets:
        obj.travel
    #Run updates to handle cooldowns etc.
    player.update()
    all_sprites.update()

    gameWindow.fill(white)
    #Draw stuff here
    gameWindow.blit(player.image, player.rect)
    all_sprites.draw(gameWindow)
    for i in range(len(zombies)):
        gameWindow.blit(zombies[i].image, zombies[i].rect)
        zombies[i].move()
        zombies[i].update()
    #End Drawing Stuff
    pygame.display.update()
    clock.tick(fps)


pygame.quit
quit()


