import pygame as pg
import random

if __name__ == '__main__':
    running = True
    pg.init()
    screen = pg.display.set_mode((600, 600))
    screen_rect = screen.get_rect()
    clock = pg.time.Clock()
    timer = 0
    day = (83, 151, 207)
    night = (33, 48, 61)
    delay = 2000
    sky_colour = day
    state = [day, night]

    while running:
        screen.fill(sky_colour)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        now = pg.time.get_ticks()
        #delay = pg.time.delay(2000)
        while 1000 < (now - timer):
            sky_colour = night
            timer = now + 2000
            #timer = (now + 2000)  # timer is shifted 2x to be ahead of now
        while 1000 < (timer - now):
            timer = now
            sky_colour = day
        #else:
        #    print("sky_cycle error")

        pg.display.update()
        clock.tick(60)
