"""
Question:
In a library system:
Responsibility 1: Manage book details.
Responsibility 2: Issue books to a user.
Responsibility 3: Track overdue fines.
"""

# Manage book Details
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
# Issue/return book to user
class BookIssueService:
    def __init__(self):
        self.book_issued = {}

    def book_issued_to(self, book, user):
        self.book_issued[book.isbn] = user
        print(f"Book {book.title} issused to {user} ")

    def book_return(self, book):
        if book.isbn in self.book_issued:
            self.book_issued.pop(book.isbn)
            print(f"Book {book.title} with id {book.isbn} returned")
        else:
            print(f"Book {book.title} never issued")

class FineCalculator:
    @staticmethod
    def fine_calculator(days_late=0):
        fine_per_day = 2
        return fine_per_day * days_late

if __name__ == "__main__":
    book1 = Book("Dark","Ramy", 1)
    book2 = Book("Jumangi", "Rock", 3)
    book3 = Book("Ramayan", "Valmiki", 5)

    issue = BookIssueService()
    issue.book_issued_to(book1, "Ram")
    issue.book_issued_to(book2,"Shyam")

    issue.book_return(book1)
    print(f"Fine To be Paid = {FineCalculator.fine_calculator(3)} Rs.")