from pathlib import Path
import json

class Robot:

    def __init__(self, name=""):
        self.name = name

    def say_hi(self):
        print(f"Hi, I'm {self.name} the robot.")

# Create an instance of Robot.
robot = Robot('Marvin')

# Convert the data to JSON, and save it.
robot_data = json.dumps(robot)
path = Path("robot.json")
path.write_text(robot_data)