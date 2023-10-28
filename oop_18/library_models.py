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

class Magazine(Resource):
    def __init__(self, title="", issue=""):
        self.title = title
        self.issue = issue
        super().__init__(resource_type="magazine")

    def get_info(self):
        return f"{self.title}, issue {self.issue}"

class Patron:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self, name="", resources=None):
        self.name = name

        if resources is None:
            self.resources = []
        else:
            self.resources = resources

    def get_books(self):
        books = [
            r for r in self.resources
            if r.resource_type == "book"
        ]
        return books

    def show_books(self):
        print(f"All books in {self.name}:")
        for book in self.get_books():
            info = book.get_info()
            print(f"- {info} ({book.get_status()})")

    def get_magazines(self):
        magazines = [
            r for r in self.resources
            if r.resource_type == "magazine"
        ]
        return magazines

    def show_magazines(self):
        print(f"All magazines in {self.name}:")
        for magazine in self.get_magazines():
            info = magazine.get_info()
            print(f"- {info} ({magazine.get_status()})")