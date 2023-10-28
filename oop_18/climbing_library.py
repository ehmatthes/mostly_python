from library_models import Library, Book, Magazine, Patron

# Create a library.
library = Library(name="The Climber's Library")

# Create some books.
book = Book(
    title="Freedom of the Hills",
    author="The Mountaineers",
    )
library.resources.append(book)

book = Book(
    title="Learning to Fly",
    author="Steph Davis",
)
library.resources.append(book)

# Show all books.
library.show_books()

# Lend a book.
birdie = Patron("Birdie")
freedom_hills = library.get_books()[0]
freedom_hills.lend(birdie)

# Show all books.
library.show_books()

# Create some magazines.
for issue_num in range(70, 84):
    magazine = Magazine(title="Alpinist", issue=issue_num)
    library.resources.append(magazine)

# Loan the latest issue.
current_issue = library.get_magazines()[-1]
current_issue.lend(birdie)

# Show magazines.
library.show_magazines()