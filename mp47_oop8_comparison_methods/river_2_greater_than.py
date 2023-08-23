class River:

    def __init__(self, name, length=0):
        self.name = name
        # Length in km.
        self.length = length

    def __gt__(self, river_2):
        return self.length > river_2.length