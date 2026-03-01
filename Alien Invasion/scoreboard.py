import pygame.font
from pygame.sprite import Group

from ship import Ship


# noinspection PyTypeChecker,PyAttributeOutsideInit
class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize score-keeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.path = self.stats.path

        # Font settings for scoring information
        self.text_color = (225, 225, 225)
        self.font = pygame.font.SysFont('agencyfb', 30)

        # Prepare initial score images
        self.prep_score()
        self.prep_highscore()
        self.prep_alltime_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"SCORE: {rounded_score:,}"
        self.score_image = self.font.render(
            score_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def check_highscores(self):
        """Check to see if there's a new highscore."""
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prep_highscore()

        if self.stats.score > self.stats.alltime_highscore:
            self.path.write_text(str(self.stats.score))
            self.stats.alltime_highscore = self.stats.score
            self.prep_alltime_highscore()

    def prep_highscore(self):
        """Turn the highscore into a rendered image."""
        highscore = round(self.stats.highscore, -1)
        highscore_str = f"HIGHSCORE: {highscore:,}"
        self.highscore_image = self.font.render(
            highscore_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # center the highscore at the top of the screen
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.score_rect.top

    def prep_alltime_highscore(self):
        """Turn the highscore into a rendered image."""
        alltime_highscore = round(self.stats.alltime_highscore, -1)
        alltime_highscore_str = f"ALL-TIME HIGHSCORE: {alltime_highscore:,}"
        self.alltime_highscore_image = self.font.render(
            alltime_highscore_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        self.alltime_highscore_rect = self.alltime_highscore_image.get_rect()
        self.alltime_highscore_rect.centerx = self.highscore_rect.centerx
        self.alltime_highscore_rect.midtop = self.highscore_rect.midbottom

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = self.stats.level
        self.level_image = self.font.render(
            f"LEVEL {level_str}",
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_stats(self):
        """Draw the scores, level, and remaining ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(
            self.alltime_highscore_image,
            self.alltime_highscore_rect,
        )
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
