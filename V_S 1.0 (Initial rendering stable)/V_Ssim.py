#V_S sim is the file contain most simulation function within classes.
import pygame as pg
import sys
from V_Spic import *
from V_Senvi import Envi
from V_Ssetting import world_size, tile_size
from V_Scam import Camera


#gridlenght_x

class Sim():
    def __init__(self,screen,clock): # Init method from main attributes
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size() # getting height and width
        # Limitation and size of the world
        self.envi = Envi( world_size, world_size, self.width, self.height)

        # Camera variables
        self.camera = Camera(self.width,self.height)


    # Running function where variables are converted to classes.
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    # Loop and exit function
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
        cursor_state = False
        if pg.mouse.get_focused():
            cursor_state = True
        elif not pg.mouse.get_focused():
            cursor_state = False
        if cursor_state:
            self.camera.update()

    # Draw function
    def draw(self):
        self.screen.fill(day)
        self.screen.blit(self.envi.grass_group, (self.camera.scroll.x,self.camera.scroll.y))
        #self.screen.blit(self.envi.oak_tree_group, (self.camera.scroll.x, self.camera.scroll.y))
        for x in range(self.envi.gridlength_x):
            for y in range (self.envi.gridlength_y):
                render_coord = self.envi.envi[x][y]["render_coord"]
                # Rectangle grid node
                #node = self.envi.envi[x][y]["node_rect"]
                #rect = pg.Rect(node[0][0], node[0][1], tile_size, tile_size)
                #pg.draw.rect(self.screen, (255,255,255), rect, 1) # Outline of grid colour

                # Isometric grid node
                #isonode = self.envi.envi[x][y]["node_poly"]
                #isonode = [(x + self.width / 2, y + self.height / 16) for x, y in isonode]
                #pg.draw.polygon(self.screen, (0,0,0), isonode, 1) #Outline colour of the grid frame.

                tile = self.envi.envi[x][y]["tile"]
                if tile != "":
                   self.screen.blit(self.envi.node[tile],(render_coord[0] + self.envi.grass_group.get_width() / 2 + self.camera.scroll.x,
                                                           render_coord[1] + self.height/48 + self.camera.scroll.y))

                # Isometric topdown grid node
                #isonodeTD = self.envi.envi[x][y]["nodeTD_poly"]
                #isonodeTD = [(x + self.width / 2, y + self.height / 16) for x, y in isonodeTD]
                #pg.draw.polygon(self.screen, (255, 255, 255), isonodeTD, 1)  # Outline colour of the grid frame.

                # Grass node rendering (singular)
                #self.screen.blit(self.envi.node["grass_node"], (render_coord[0] + self.width/2 + self.camera.scroll.x,
                # render_coord[1] + self.height/16 + self.camera.scroll.y))
                # oak tree rendering (singular)
                #self.screen.blit(self.envi.node["oak_tree"], (render_coord[0] * self.envi.grass_group.get_width()/2 + self.camera.scroll.x,
                # render_coord[1] + self.height/48 + self.camera.scroll.y))



        pg.display.flip()
