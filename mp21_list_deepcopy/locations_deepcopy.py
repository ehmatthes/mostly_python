from copy import deepcopy

class Location:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

location_1 = Location(0, 10)
location_2 = Location(0, 20)
location_3 = Location(0, 30)

locations = [location_1, location_2, location_3]
original_locations = deepcopy(locations)

print(f"current locations:\t{locations}")
print(f"original locations:\t{original_locations}")

# Shift all locations to the right.
location_1.x += 10
location_2.x += 10
location_3.x += 10

print(f"current locations:\t{locations}")
print(f"original locations:\t{original_locations}")