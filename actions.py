import math

def calcMove(speed, fromx, fromy, tox, toy):  # I'm going this fast, want to get from(x,y) to(x,y)
    run = fromx - tox
    rise = toy - fromy
    length = math.sqrt((rise * rise) + (run * run))
    unitx = run / length
    unity = rise / length
    fromx -= int(unitx * speed)
    fromy += int(unity * speed)
    return (fromx, fromy)