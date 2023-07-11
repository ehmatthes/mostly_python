class Robot:
    """A class representing simple robots."""

    def __init__(self, name=""):
        self.name = name
        self.type = "drone"
        self.mass_grams = 249

    def say_hello(self):
        print(f"Hi, I'm {self.name}!")
        print(f"I'm a {self.type}.")
        print(f"I have a mass of {self.mass_grams}g.")

my_robot = Robot("William")
my_robot.say_hello()