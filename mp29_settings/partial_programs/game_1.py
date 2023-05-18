from alien_1 import Alien

class Game:

    def __init__(self):
        self.alien_speed = 5
        self.alien_direction = 1

        self.alien = Alien(self)

    def show_settings(self):
        print("\nIn Game:")
        print(f"  alien speed: {self.alien_speed}")
        print(f"  alien direction: {self.alien_direction}")

if __name__ == '__main__':
    game = Game()
    game.show_settings()
    game.alien.show_settings()
