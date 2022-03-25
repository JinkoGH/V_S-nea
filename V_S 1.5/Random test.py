import random
import pygame as pg

pg.init()
RED = pg.Color('red')
screen = pg.display.set_mode((800, 400))
width, height = screen.get_size()
clock = pg.time.Clock()
done = False

sides = ['top', 'bottom', 'left', 'right']
weights = [width, width, height, height]

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    side = random.choices(sides, weights)[0]

    if side == 'top':
        y = 0
        x = random.randrange(width-4)
    elif side == 'bottom':
        y = height-4
        x = random.randrange(width-4)
    elif side == 'left':
        x = 0
        y = random.randrange(height-4)
    elif side == 'right':
        x = width - 4
        y = random.randrange(height - 4)

    pg.draw.rect(screen, RED, (x, y, 4, 4))
    pg.display.flip()
    clock.tick(30)