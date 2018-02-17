import pygame
import random
import math
from character_classes import *
from actions import *

#some game initializers
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



## initialize our players and enemies
bullets = []
zombies = []
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group
player = playerActive(blue)
for i in range(2):
    z = Zombie(red,gameWidth,gameHeight,player)
    all_sprites.add(z) 
    mobs.add(z)
zombies.append(bigZombie(yellow,gameWidth,gameHeight,player))
all_sprites = pygame.sprite.Group()


#Game Start
gameActive = True
fps = 60
while gameActive: #Game loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameActive = False
    #Get Key presses
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
        zombies.append(Zombie(red,gameWidth,gameHeight,player))
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
        zombies[i].move(player)
        zombies[i].update()
    #End Drawing Stuff
    pygame.display.update()
    clock.tick(fps)

pygame.quit
quit()