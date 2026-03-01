import pygame.font


class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg, location, w, h, b_rgb, t_rgb, font_s,
                 font_n=None, align=None):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of the button
        self.width, self.height = w, h
        self.button_color = b_rgb
        self.text_color = t_rgb
        self.font = pygame.font.SysFont(font_n, font_s)

        # Build the button's rect object
        self.x, self.y = location
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self._set_button_location(align)

        # The button message needs to be prepped only once
        self._prep_message(msg)

    def _set_button_location(self, screen_loc):
        """Initialize the button's rect location based on screen location."""
        if screen_loc == 'center':
            self.rect.center = self.screen_rect.center
        elif screen_loc == 'midbottom':
            self.rect.midbottom = self.screen_rect.midbottom
        elif screen_loc == 'midtop':
            self.rect.midtop = self.screen_rect.midtop
        elif screen_loc == 'midleft':
            self.rect.midleft = self.screen_rect.midleft
        elif screen_loc == 'midright':
            self.rect.midright = self.screen_rect.midright
        elif screen_loc == 'topleft':
            self.rect.topleft = self.screen_rect.topleft
        elif screen_loc == 'topright':
            self.rect.topright = self.screen_rect.topright
        elif screen_loc == 'bottomleft':
            self.rect.bottomleft = self.screen_rect.bottomleft
        elif screen_loc == 'bottomright':
            self.rect.bottomright = self.screen_rect.bottomright

    def _prep_message(self, msg):
        """Turn msg into a rendered image and center text on button."""
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
