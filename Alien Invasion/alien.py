import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a singe alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and its starting position."""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen

        # Load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien_spaceship.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True is an alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
