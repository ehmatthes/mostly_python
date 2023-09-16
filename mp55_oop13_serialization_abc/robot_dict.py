from pathlib import Path
import json

robot = {'name': 'Marvin'}

robot_data = json.dumps(robot)
path = Path("robot.json")
path.write_text(robot_data)