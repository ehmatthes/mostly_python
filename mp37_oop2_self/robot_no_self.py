def make_robot(name=""):
    """Make a robot."""
    robot_dict = {
        "name": name,
        "type": "drone",
        "mass_grams": 249,
    }

    return robot_dict

def say_hello(robot_dict):
    """Make a robot say hello."""
    print(f"Hi, I'm {robot_dict['name']}.")
    print(f"I'm a {robot_dict['type']}.")
    print(f"I have a mass of {robot_dict['mass_grams']}g.")

my_robot = make_robot("William")
say_hello(my_robot)