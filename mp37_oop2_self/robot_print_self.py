class Robot:
    """A class representing simple robots."""

    def __init__(self, name=""):
        self.name = name
        print(self)

    def say_hello(self):
        print(f"Hi, I'm {self.name}!")

my_robot = Robot("William")