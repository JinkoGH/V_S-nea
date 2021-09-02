#importations
import pygame
import sys
import time


#from Login_system1_2 import *
# Initialising pygame to access all functions
pygame.init()

#Display screen
screen = pygame.display.set_mode((1600,900))
screen_size = (1600,900)
# Window features
pygame.display.set_caption(("Vegetation Simulation"))
icon = pygame.image.load('NEA tree icon.png')
pygame.display.set_icon(icon)
display = pygame.Surface((300, 300))
#timer
clock = pygame.time.Clock()
timer = 0

#Nodes
grass_img = pygame.image.load("Grass node.png")
tile_size = grass_img.get_width()
#map function



#background colours:
day = (83, 151, 207)
night = (33, 48, 61)


#updating the display
open = True
while open:
    # loop and exit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

    #day night cycle
    screen.fill(day)
    #Visualising map
    display.fill((0, 0, 0))

    screen.blit(grass_img,(100,200))


    pygame.display.update()
    clock.tick(60)



