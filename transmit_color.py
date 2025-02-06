import pygame
import sys

from time import sleep

def display_transmission(constellation):

    pygame.init()

    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('Modulation Transmission')

    sleep(3)

    points = constellation.points

    for p in points:
        screen.fill(p.get_color())
        pygame.display.flip()
        sleep(1)

        screen.fill('black')
        pygame.display.flip()
        sleep(1)

    pygame.quit()
    sys.exit()

