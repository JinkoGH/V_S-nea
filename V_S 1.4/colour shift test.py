import pygame
import itertools

pygame.init()

screen = pygame.display.set_mode((800, 600))
day = (83, 151, 207)
night = (33, 48, 61)
colors = itertools.cycle([day, night])

clock = pygame.time.Clock()

base_color = next(colors)
next_color = next(colors)
current_color = base_color

FPS = 60
day_length = 400
step = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    step += 1
    if step < day_length:
        # (y-x)/number_of_steps calculates the amount of change per step required to
        # fade one channel of the old color to the new color
        # We multiply it with the current step counter
        current_color = [x + (((y - x) / day_length) * step) for x, y in
                         zip(pygame.color.Color(base_color), pygame.color.Color(next_color))]
    else:
        step = 1
        base_color = next_color
        next_color = next(colors)

    screen.fill(current_color)
    # pygame.draw.circle(screen, current_color, screen.get_rect().center, 100)
    # screen.blit(text, (230, 100))
    pygame.display.update()
    clock.tick(FPS)