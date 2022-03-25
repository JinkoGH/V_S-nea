# V_S sim is the file contain most simulation function within classes.
# Importations
import random
import pygame as pg
import sys
import itertools

# Linking files and classes
from V_Spic import *
from V_Senvi import Envi
from V_Ssetting import world_size, tile_size, day_length
from V_Scam import Camera


class Sim():
    def __init__(self, screen, clock):  # Init method from main attributes
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()  # getting height and width
        # Limitation and size of the world
        self.envi = Envi(world_size, world_size, self.width, self.height)

        # Camera variables
        self.camera = Camera(self.width, self.height)

        # Time variables
        self.timer = 0
        self.step = 0

        # Initial adjustable variable states
        self.colours = itertools.cycle([day, night])

        # colour reference points
        self.base_colour = next(self.colours)
        self.next_colour = next(self.colours)
        self.current_colour = self.base_colour

    # Running function which allows functions in Sim to be looped under the main loop
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    # Program event loop

    def events(self):
        # Escape function to close program
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()


            # TESTING PURPOSES (TEMP)
            # print(pg.mouse.get_focused())

    # Update function

    def update(self):
        # Cursor window active status
        cursor_state = False
        if pg.mouse.get_focused():
            cursor_state = True
        elif not pg.mouse.get_focused():
            cursor_state = False
        if cursor_state:
            self.camera.update()

    # Draw function

    def draw(self):
        # day and night cycle

        self.step += 1
        if self.step < day_length:
            self.current_colour = [x + (((y - x) / day_length) * self.step) for x, y in
                             zip(pg.color.Color(self.base_colour), pg.color.Color(self.next_colour))]
        else:
            self.step = 0
            self.base_colour = self.next_colour
            self.next_colour = next(self.colours)

        self.screen.fill(self.current_colour)

        """Group rendering"""
        self.screen.blit(self.envi.grass_group, (self.camera.scroll.x, self.camera.scroll.y))
        # self.screen.blit(self.envi.oak_tree_group, (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.envi.gridlength_x):
            for y in range(self.envi.gridlength_y):

                render_coord = self.envi.envi[x][y]["render_coord"]
                """Grid rendering"""
                # Rectangle grid node
                # node = self.envi.envi[x][y]["node_rect"]
                # rect = pg.Rect(node[0][0], node[0][1], tile_size, tile_size)
                # pg.draw.rect(self.screen, (255,255,255), rect, 1) # Outline of grid colour

                # Isometric grid node
                # isonode = self.envi.envi[x][y]["node_poly"]
                # isonode = [(x + self.width / 2, y + self.height / 16) for x, y in isonode]
                # pg.draw.polygon(self.screen, (0,0,0), isonode, 1) #Outline colour of the grid frame.

                # Isometric topdown grid node
                # isonodeTD = self.envi.envi[x][y]["nodeTD_poly"]
                # isonodeTD = [(x + self.width / 2, y + self.height / 16) for x, y in isonodeTD]
                # pg.draw.polygon(self.screen, (255, 255, 255), isonodeTD, 1)  # Outline colour of the grid frame.

                """"Singular rendering"""
                # Tree rendering
                entity = self.envi.envi[x][y]["entity"]

                # now = pg.time.get_ticks()
                # if now - self.cooldown > (day_length/2):
                #     r = random.randint(1, 2)
                #     if r != 2:
                #         entity = "oak_tree"
                #     else:
                #         entity = "empty"
                #     self.cooldown = now

                # Rendering of non perlin affected objects
                if entity != "empty":
                    self.screen.blit(self.envi.node[entity],
                                     (render_coord[0] + self.envi.grass_group.get_width() / 2 + self.camera.scroll.x,
                                      render_coord[1] + self.height / 48 + self.camera.scroll.y))

        # Updating the screen after iteration
        pg.display.flip()
