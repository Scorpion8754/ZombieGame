import pygame
import time
import os
import random
import math
os.chdir(os.path.dirname(__file__))
display_width = 1280
display_height = 720



pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Zombie')
clock = pygame.time.Clock()
zombieList = []

zombieCount = 1
health = 100
#Define some colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

playerImg = pygame.image.load(os.path.join(os.path.dirname(__file__), "circle"))
playerImg = pygame.transform.scale(playerImg, (35, 35))
player_width = 50
player_height = 50

def calcMove(speed,fromx,fromy,tox,toy): #I'm going this fast, want to get from(x,y) to(x,y)
    run = fromx - tox
    rise = toy - fromy
    length = math.sqrt((rise*rise) + (run*run))
    unitx = run/length
    unity = rise/length
    fromx -= int(unitx * speed)
    fromy += int(unity * speed)
    return(fromx,fromy)

def zombie(snakelist):
    for XnY in snakelist:
        pygame.draw.circle(gameDisplay, red, [XnY[0],XnY[1]], 15)

def addZombie():
            zombx = random.randrange(0,display_width)
            zombu = random.randrange(0,display_height)
            zombies = []
            zombies.append(zombx)
            zombies.append(zombu)
            
            zombieList.append(zombies)

def player(x,y):
    gameDisplay.blit(playerImg,(x,y))

def message_display(text,fontsz): 
    font = pygame.font.Font('freesansbold.ttf', fontsz) 
    gameDisplay.blit(font.render(text, True, (0,0,0)), ((display_width/2)-len(text)*32,0))
    pygame.display.update()
def death():
            message_display("WASTED",115)
            time.sleep(2)
            game_loop()
def game_loop(): #game loop
    #Positioning and movement
    x = (display_width * 0.45)
    y = (display_height * 0.45)
    #zombie variables
    zombie_startx = 0
    zombie_starty = 0
    zombieLead = []
    zombieLead.append(zombie_startx)
    zombieLead.append(zombie_starty)
    zombieList.append(zombieLead)
    zombie_speed = 3
    health = 100
    health_change = 0
    gameRunning = True
    move_up = False
    move_down = False
    move_right = False
    move_left = False
    while gameRunning: 
        for event in pygame.event.get(): #event handling
            if event.type == pygame.QUIT:
                gameRunning = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN: # Handle keypresses
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_d:
                    move_right = True    
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True
                if event.key == pygame.K_0:
                    addZombie()
                    print(zombieList)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False    
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False
        #move
        if(move_up == True):
            y -= 5
        if(move_left == True):
            x -= 5
        if(move_down == True):
            y += 5
        if(move_right == True):
            x += 5
        health =+ health_change
        gameDisplay.fill(white)
        
        

        zombie(zombieList) 
        if len(zombieList) > zombieCount:
            del zombieList[0]
            print(zombieList)



        goto = calcMove(zombie_speed,zombieList[0][0],zombieList[0][1],x,y)
        zombie_startx = goto[0]
        zombie_starty = goto[1]




        player(x,y)
        #Define edge
        if x <= 0:
            x = 0
        elif x >= display_width - (player_width):
            x = display_width - (player_width)
        if y <= 0:
            y = 0
        elif y >= display_height - (player_height):
            y = display_height - player_height
        if health < 0:
            death()
            gameRunning = False

        
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()