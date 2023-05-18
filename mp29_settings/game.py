from alien import Alien

class Game:

    def __init__(self):
        self.settings = {
            'alien_speed': 5,
            'alien_direction': 1
        }

        self.alien = Alien(self)

    def show_settings(self):
        print("\nIn Game:")
        print(f"  alien speed: {self.settings['alien_speed']}")
        print(f"  alien direction: {self.settings['alien_direction']}")

    def increase_speed(self):
        self.settings['alien_speed'] += 1

    def change_direction(self):
        self.settings['alien_direction'] *= -1

if __name__ == '__main__':
    game = Game()
    game.show_settings()
    game.alien.show_settings()

    game.increase_speed()
    game.change_direction()

    game.show_settings()
    game.alien.show_settings()
