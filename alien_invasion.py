import sys
import pygame

def run_game():

    # Initialize the game and create a screem object
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Invasion alienigena")

    # Initialize the game main bucle
    while True:

        # Listening keyboard or mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Making visible the latest screen
        pygame.display.flip()

run_game()
