class BonsaiTree:

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def describe_tree(self):
        msg = f"{self.name}: {self.description}"
        print(msg)

tree = BonsaiTree("Winged Elm")
tree.description = "tall, solid trunk"
tree.describe_tree()