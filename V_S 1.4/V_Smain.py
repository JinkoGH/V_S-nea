# V_S is the main python file in which all other files will communicate with each other
#  and where the main game loop runs
# Importations
import pygame as pg

# Linking files
from V_Ssim import Sim
from V_Ssetting import screen_size

def Main():
    # screen
    pg.init()
    pg.mixer.init()
    pg.display.set_caption("Vegetation Simulation")
    screen = pg.display.set_mode(screen_size)
    window_icon = pg.image.load('Images/NEA tree icon.png').convert()
    pg.display.set_icon(window_icon)
    clock = pg.time.Clock()

    # Linking Sim class
    sim = Sim(screen, clock)

    # Main program loop
    running = True
    while running:
        sim.run()

if __name__ == "__main__":
    Main()












