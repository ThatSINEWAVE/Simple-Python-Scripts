class Settings:
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Initialize static game settings."""

        # Screen settings
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (59, 68, 135)
        self.fullscreen = True

        # Ship settings
        self.default_ship_speed = 4
        self.ship_limit = 3  # not including starting ship

        # Bullet settings
        self.default_bullet_speed = 12
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 223, 0)  # RGB
        self.bullets_allowed = 10

        # Alien settings
        self.default_alien_speed = 2.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # fleet direction: 1 = right, -1 = left
        self.initial_alien_points = 50

        # Level-up settings  (multipliers)
        self.speedup_scale = 1.1  # how quickly the game speeds up
        self.score_scale = 1.5  # how quickly the alien point values increase

        self.initialise_dynamic_settings()

        # Dynamic settings
        self.ship_speed = None
        self.bullet_speed = None
        self.alien_speed = None
        self.alien_points = None

    def initialise_dynamic_settings(self):
        """Initialize settings that can change throughout the game."""
        self.ship_speed = self.default_ship_speed
        self.bullet_speed = self.default_bullet_speed
        self.alien_speed = self.default_alien_speed
        self.fleet_direction = 1  # fleet direction: 1 = right, -1 = left

        # Scoring points
        self.alien_points = self.initial_alien_points

    def increase_speed(self):
        """Increase speed and alien point values."""
        self.ship_speed *= self.speedup_scale * 1.001  # aliens speed up
        #                                                 a little more
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
