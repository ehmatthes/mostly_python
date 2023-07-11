class Robot:
    """A class representing simple robots."""

    def __init__(self, name=""):
        self.name = name
        print(self)

    def say_hello(self):
        print(f"Hi, I'm {self.name}!")
        print(self)

my_robot = Robot("William")
print(my_robot)

my_robot.say_hello()