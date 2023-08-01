class BonsaiTree:

    num_trees = 0

    @classmethod
    def count_trees(cls):
        msg = f"We have {cls.num_trees} trees in the collection."
        print(msg)

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

        BonsaiTree.num_trees += 1

    def describe_tree(self):
        msg = f"{self.name}: {self.description}"
        print(msg)

trees = []

tree = BonsaiTree("Winged Elm")
tree.description = "tall, solid trunk"
trees.append(tree)

tree = BonsaiTree("El Arbol Murcielago")
tree.description = "short, open trunk"
trees.append(tree)

tree = BonsaiTree("Mt. Mitchell")
tree.description = "small mountain forest"
trees.append(tree)

for tree in trees:
    tree.describe_tree()

tree.count_trees()