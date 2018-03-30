import math
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Zombie Game"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


def calcMove(speed, fromx, fromy, tox, toy):  # I'm going this fast, want to get from(x,y) to(x,y)
    run = fromx - tox
    rise = toy - fromy
    length = math.sqrt((rise * rise) + (run * run))
    unitx = run / length
    unity = rise / length
    vx = int(unitx * speed)
    vy = int(unity * speed)
    return (vx, vy)

#Player Settings
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'player_gun.png'