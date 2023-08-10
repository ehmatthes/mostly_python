class BonsaiTree:

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def describe_tree(self):
        msg = f"{self.name}: {self.description}"
        print(msg)
    
    def __repr__(self):
        if self.description:
            return (f"BonsaiTree(name={self.name}, "
                    f"description={self.description})")
        else:
            return(f"BonsaiTree(name={self.name})")
