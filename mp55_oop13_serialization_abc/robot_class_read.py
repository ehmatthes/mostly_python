import json
from pathlib import Path

from marshmallow import Schema, fields, post_load

class Robot:

    def __init__(self, name=""):
        self.name = name

    def say_hi(self):
        print(f"Hi, I'm {self.name} the robot.")

class RobotSchema(Schema):
    name = fields.Str()

    @post_load
    def make_robot(self, data, **kwargs):
        return Robot(**data)

# Read in the data.
path = Path("robot.json")
robot_data = path.read_text()
robot_data = json.loads(robot_data)

# Use RobotSchema to deserialize the data.
schema = RobotSchema()
robot = schema.load(robot_data)

# Use the robot.
robot.say_hi()
print(robot)