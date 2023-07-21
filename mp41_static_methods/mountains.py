class Mountain:

    def __init__(self, name="", elev_meters=0):
        self.name = name
        self.elev_meters = elev_meters

    def describe_mountain(self):
        msg = f"{self.name} is {self.elev_meters:,} meters tall."
        print(msg)

my_mountain = Mountain("Mt. Verstovia", 1022)
my_mountain.describe_mountain()