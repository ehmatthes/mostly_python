class Book:
    def __init__(self, title="", author=""):
        self.title = title
        self.author = author

    def get_info(self):
        return f"{self.title}, by {self.author}"

class Library:
    def __init__(self, name="", books=None):
        self.name = name

        if books is None:
            self.books = []
        else:
            self.books = books

    def show_books(self):
        print(f"All books in {self.name}:")
        for book in self.books:
            info = book.get_info()
            print(f"- {info}")

if __name__ == "__main__":
    my_library = Library(name="The Climber's Library")

    book = Book(
        title="Freedom of the Hills",
        author="The Mountaineers"
    )
    my_library.books.append(book)

    book = Book(
        title = "Learning to Fly",
        author = "Steph Davis",
    )
    my_library.books.append(book)

    my_library.show_books()