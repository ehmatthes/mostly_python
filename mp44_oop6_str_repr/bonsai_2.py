class BonsaiTree:

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def describe_tree(self):
        msg = f"{self.name}: {self.description}"
        print(msg)
    
    def __str__(self):
        return self.name

tree = BonsaiTree("Winged Elm")
print(tree)
