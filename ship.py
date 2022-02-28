import pygame

class Ship:
    """It is used to manage the behavior of the ship"""

    def __init__(self, screen):
        """It initialize the ship and set his start position"""

        self.screen = screen

        # Load the ship image and get his rect
        self.image = pygame.image.load("img/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # each new ship start in the lower center part of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """It draw the ship in his currently location"""
        self.screen.blit(self.image, self.rect)