# V_Senvi will hold all code related towards the nodes and the grid system of the simulation.
# Importations
import pygame as pg
import random
import noise

# Linking files and classes
from V_Ssetting import tile_size, day_length
from V_Spic import *



print("random values generated:")

class Envi():
    # Initialising dimensions of nodes and grid.
    def __init__(self, gridlength_x, gridlength_y, width, height):
        # Initialising dimensions
        self.gridlength_x = gridlength_x
        self.gridlength_y = gridlength_y
        self.width = width
        self.height = height

        # noise values
        ran_perlin_scale = random.randint(10, 20)
        self.perlin_scale = ran_perlin_scale
        upper_p = random.randint(20, 30)
        self.ran_upper_p = upper_p
        lower_p = random.randint(-40, -25)
        self.ran_lower_p = lower_p
        print("perlin scale is:", ran_perlin_scale)
        print("upper perlin value is", upper_p)
        print("lower perlin value is", lower_p)

        # initialising the node
        self.node = self.loadimages()
        # rendering collections
        self.grass_group = pg.Surface((gridlength_x * tile_size * 2,
                                       gridlength_y * tile_size + tile_size * 3.25)).convert_alpha()
        #self.oak_tree_group = pg.Surface((gridlength_x * tile_size * 2 , gridlength_y * tile_size + tile_size * 3.25)).convert_alpha()

        # Timer
        self.timer = 0

        # Starting up an environment
        self.envi = self.create_envi()


    # Function for creating an environment.
    def create_envi(self):
        envi = []
        for grid_x in range(self.gridlength_x):
            envi.append([])
            for grid_y in range(self.gridlength_y):
                envi_tile = self.grid_to_envi(grid_x,grid_y)
                envi[grid_x].append(envi_tile)

                render_coord = envi_tile["render_coord"]
                # Pre rendering grass nodes
                self.grass_group.blit(self.node["grass_node"],
                                      (render_coord[0] + self.grass_group.get_width()/2, render_coord[1] + self.height / 16))
                self.grass_group.set_colorkey(black)

        return envi

    def grid_to_envi(self, grid_x, grid_y):
        # Getting the the corners of the square nodes
        rect = [
            (grid_x*tile_size, grid_y*tile_size),
            (grid_x*tile_size + tile_size, grid_y*tile_size),
            (grid_x*tile_size + tile_size, grid_y*tile_size + tile_size),
            (grid_x*tile_size, grid_y*tile_size + tile_size)
        ]

        # Linking the iso convert function to a variable
        iso_poly = [self.node_to_iso(x, y) for x, y in rect]
        isoTD_poly = [self.node_to_isoTD(x, y) for x, y in rect]

        # Getting the minimum coordinates for rendering entities
        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        # temp
        #upper_p = random.randint(20, 30)
        #lower_p = random.randint(-35, -15)


        # Random tile selection based of number generated

        r = random.randint(1, 100)
        perlin = 100 * noise.pnoise2(grid_x / self.perlin_scale, grid_y / self.perlin_scale)
        if (perlin >= self.ran_upper_p) or (perlin <= self.ran_lower_p):
            entity = "oak_tree"

        else:
            if r == 1:
                entity = "oak_tree"

            else:
                entity = "empty"
        dictionary = {
            "grid": [grid_x, grid_y],
            "node_rect": rect,
            "node_poly": iso_poly,
            "nodeTD_poly": isoTD_poly,
            "render_coord": [minx, miny],
            "entity": entity
        }
        return dictionary



    # Function for changing the original nodes' coordinates to an asymmetric coordinates for the asymmetric layout
    def node_to_iso(self, x, y):
        iso_x = (x - y)
        iso_y = (x + y)/2
        return iso_x, iso_y

    def node_to_isoTD(self, x, y):
        iso_xTD = (x - y)
        iso_yTD = (x + y)
        return iso_xTD, iso_yTD

    # Function for getting the image files to be recognised in pygame.
    def loadimages(self):
        grass_node = pg.image.load("Images/grass node 3.0.png").convert_alpha()
        oak_tree = pg.image.load("Images/oak tree(outline).png").convert_alpha()
        return {"grass_node": grass_node,
                "oak_tree": oak_tree}
















