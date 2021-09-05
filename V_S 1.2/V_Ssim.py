# V_S sim is the file contain most simulation function within classes.
# Importations
import random
import pygame as pg
import sys

# Linking files and classes
from V_Spic import *
from V_Senvi import Envi
from V_Ssetting import world_size, tile_size, day_length
from V_Scam import Camera

class Sim():
    def __init__(self, screen, clock): # Init method from main attributes
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size() # getting height and width
        # Limitation and size of the world
        self.envi = Envi(world_size, world_size, self.width, self.height)

        # Camera variables
        self.camera = Camera(self.width, self.height)

        # Timer
        self.timer = 0

        # Initial adjustable variable states
        self.sky_colour = day

    # Running function which allows functions in Sim to be looped under the main loop
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            #self.day_update()
            #self.night_update()
            self.draw()


    # Program event loop

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

            # TESTING PURPOSES (TEMP)
            #print(pg.mouse.get_focused())

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
        self.screen.fill(self.sky_colour)
        now = pg.time.get_ticks()
        while (day_length - (day_length/10)) <= (now - self.timer) <= day_length:
            self.sky_colour = night
            self.timer = now + (day_length * 2)  # timer is shifted 2x to be ahead of now
        while (day_length - (day_length/10)) <= (self.timer - now) <= day_length:
            self.sky_colour = day
            self.timer = now

        """Visualisation"""
        # First 3 seconds with day length as 1 second long
        # timer        now        day/night ~dif1  ~dif2
        # timer = 0    now > 0    day       0     0
        # timer = 0    now < 1000 day       1000  -1000
        # timer = 3000 now > 1000 night     -2000 2000
        # timer = 3000 now < 2000 night     -1000 1000
        # timer = 2000 now > 2000 day       0     0
        # timer = 2000 now < 3000 day       1000  -1000
        # timer = 5000 now > 3000 night     -2000 2000

        """Group rendering"""
        self.screen.blit(self.envi.grass_group, (self.camera.scroll.x, self.camera.scroll.y))
        #self.screen.blit(self.envi.oak_tree_group, (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.envi.gridlength_x):
            for y in range (self.envi.gridlength_y):
                render_coord = self.envi.envi[x][y]["render_coord"]

                """Grid rendering"""
                # Rectangle grid node
                #node = self.envi.envi[x][y]["node_rect"]
                #rect = pg.Rect(node[0][0], node[0][1], tile_size, tile_size)
                #pg.draw.rect(self.screen, (255,255,255), rect, 1) # Outline of grid colour

                # Isometric grid node
                #isonode = self.envi.envi[x][y]["node_poly"]
                #isonode = [(x + self.width / 2, y + self.height / 16) for x, y in isonode]
                #pg.draw.polygon(self.screen, (0,0,0), isonode, 1) #Outline colour of the grid frame.

                # Isometric topdown grid node
                # isonodeTD = self.envi.envi[x][y]["nodeTD_poly"]
                # isonodeTD = [(x + self.width / 2, y + self.height / 16) for x, y in isonodeTD]
                # pg.draw.polygon(self.screen, (255, 255, 255), isonodeTD, 1)  # Outline colour of the grid frame.

                """"Singular rendering"""

                # Initial rendering of trees

                tile = self.envi.envi[x][y]["tile"]
                if tile != "empty":
                   self.screen.blit(self.envi.node[tile],(render_coord[0] + self.envi.grass_group.get_width() / 2 + self.camera.scroll.x,
                                                          render_coord[1] + self.height/48 + self.camera.scroll.y))

                # Grass node rendering (singular)
                #self.screen.blit(self.envi.node["grass_node"], (render_coord[0] + self.width/2 + self.camera.scroll.x,
                # render_coord[1] + self.height/16 + self.camera.scroll.y))
                # oak tree rendering (singular)
                #self.screen.blit(self.envi.node["oak_tree"], (render_coord[0] * self.envi.grass_group.get_width()/2 + self.camera.scroll.x,
                # render_coord[1] + self.height/48 + self.camera.scroll.y))

        pg.display.flip()

