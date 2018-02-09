import pygame
import time
import os
import random
import math
#os.chdir(os.path.dirname(__file__))


#Set our working configs
#resolution
## to do: Autodect desktop resolution and match it, add command line arguments to set resolution upon launching game
display_width = 1280
display_height = 720

#Set asset directories
gameRootDir = os.path.dirname(os.path.realpath(__file__))
charactersDir = os.path.join(gameRootDir, "assets/art/characters")
sceneryDir = os.path.join(gameRootDir, "assets/art/scenery")
audioEffectsDir = os.path.join(gameRootDir, "assets/sound/effects")
musicDir = os.path.join(gameRootDir, "assets/sound/music")



#main function block
#### Eventually we want to make this block contain only the main game loop. (all function definitions should be moved outside of this block.)
def main():
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

    playerImg = pygame.image.load(os.path.join(charactersDir, "player/circle"))
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
            zombieLead = []
            zombieLead.append(zombie_startx)
            zombieLead.append(zombie_starty)
            zombieList.append(zombieLead)
            

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

if __name__ == "__main__":
    # execute only if run as a script
    try:
        main()
    except Exception as ex:
        print("Oh shit the game has crashed, here is the error")
        print(ex)     