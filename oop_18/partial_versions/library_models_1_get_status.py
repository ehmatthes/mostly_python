class Resource:
    def __init__(self, resource_type):
        self.resource_type = resource_type
        self.current_borrower = None

    def lend(self, patron):
        self.current_borrower = patron

    def return_resource(self):
        self.current_borrower = None

    def get_status(self):
        if self.current_borrower:
            return "on loan"
        else:
            return "available"

class Book(Resource):
    def __init__(self, title="", author=""):
        self.title = title
        self.author = author
        super().__init__(resource_type="book")

    def get_info(self):
        return f"{self.title}, by {self.author}"

class Patron:
    def __init__(self, name):
        self.name = name