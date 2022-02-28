import sys
import pygame

def verify_events():
    """Responds to mouse clicks and events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_configurations, screen, ship):
    """It update images in the screen and refresh screen"""

    # It draw screen for each bucle again
    screen.fill(game_configurations.bg_color)
    ship.blitme()

    # Making visible the latest screen
    pygame.display.flip()