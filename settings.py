class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,181,226)

        # Ship settings
        self.ship_speed = 3

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (224,33,138)
        self.bullets_allowed = 3
