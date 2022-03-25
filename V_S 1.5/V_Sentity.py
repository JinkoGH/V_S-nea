
import pygame as pg
import random
from V_Senvi import Envi
from V_Ssetting import world_size

class Oak_tree(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # image
        self.image = pg.image.load("Images/oak tree(outline).png").convert_alpha()
        self.rect = self.image.get_rect()
        #self.rect.center = [pos_x, pos_y]
    def update(self):
        pass

    oak_tree_group = pg.sprite.Group()








