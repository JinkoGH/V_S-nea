#V_Scam holds all the functions of the camera

# Importations
import pygame as pg

# Linking files and classes
from V_Ssetting import cam_speed, cam_screen_percent



class Camera:

    def __init__(self, width, height):
        # Initialising dimensions
        self.width = width
        self.height = height
        # Cursor inputs
        self.scroll = pg.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = cam_speed

    def update(self):
        # Finding the mouse position on the display
        mouse_pos = pg.mouse.get_pos()

        # Horizontal/x movement
        if mouse_pos[0] > self.width * (1 - cam_screen_percent):
            self.dx = -self.speed
        elif mouse_pos[0] < self.width * cam_screen_percent:
            self.dx = self.speed
        else:
            self.dx = 0
        # Vertical/y movement
        if mouse_pos[1] > self.height * (1 - cam_screen_percent):
            self.dy = -self.speed
        elif mouse_pos[1] < self.height * cam_screen_percent:
            self.dy = self.speed
        else:
            self.dy = 0


        # Updating the camera position
        self.scroll.x += self.dx
        self.scroll.y += self.dy