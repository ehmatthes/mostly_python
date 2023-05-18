class Alien:

    def __init__(self, game):
        self.speed = game.alien_speed
        self.direction = game.alien_direction

    def show_settings(self):
        print("\nIn Alien:")
        print(f"  alien speed: {self.speed}")
        print(f"  alien direction: {self.direction}")