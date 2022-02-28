import sys
import pygame

from config import Config

def run_game():

    # Initialize the game, the configurations and create a screem object
    pygame.init()

    game_configurations = Config()

    screen = pygame.display.set_mode(
        (game_configurations.screen_width, game_configurations.screen_height))

    pygame.display.set_caption("Invasion alienigena")

    # Initialize the game main bucle
    while True:

        # Listening keyboard or mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # It draw screen for each bucle again
        screen.fill(game_configurations.bg_color)

        # Making visible the latest screen
        pygame.display.flip()

run_game()
