class Alien:

    def __init__(self, game):
        self.settings = game.settings

    def show_settings(self):
        print("\nIn Alien:")
        print(f"  alien speed: {self.settings['alien_speed']}")
        print(f"  alien direction: {self.settings['alien_direction']}")