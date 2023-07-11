class Robot:
    """A class representing simple robots."""

    def __init__(potato, name=""):
        potato.name = name

    def say_hello(potato):
        print(f"Hi, I'm {potato.name}!")

my_robot = Robot("William")
my_robot.say_hello()