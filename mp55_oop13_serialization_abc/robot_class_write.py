from pathlib import Path

from marshmallow import Schema, fields

class Robot:

    def __init__(self, name=""):
        self.name = name

    def say_hi(self):
        print(f"Hi, I'm {self.name} the robot.")

class RobotSchema(Schema):
    name = fields.Str()

# Create an instance of Robot.
robot = Robot('Marvin')

# Use RobotSchema to serialize the data.
schema = RobotSchema()
robot_data = schema.dumps(robot)

path = Path("robot.json")
path.write_text(robot_data)