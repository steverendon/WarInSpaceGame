import pygame

from config import Config
from ship import Ship
import game_functions as gf

def run_game():

    # Initialize the game, the configurations and create a screem object
    pygame.init()

    game_configurations = Config()

    screen = pygame.display.set_mode(
        (game_configurations.screen_width, game_configurations.screen_height))

    pygame.display.set_caption("Invasion alienigena")

    # It create a ship
    ship = Ship(screen)

    # Initialize the game main bucle
    while True:

        # Listening keyboard or mouse events
        gf.verify_events()

        gf.update_screen(game_configurations, screen, ship)

run_game()
