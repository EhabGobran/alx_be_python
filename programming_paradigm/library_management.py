class Book:
    def __init__(self, title , author ,isCheckedOut):
        self.title = title
        self.author = author
        self._is_checked_out = isCheckedOut

    def get_is_checked_out(self):
        return self._is_checked_out
    

class Library:
    def __init__(self):
        self._books:Book = []

    def add_book(self , NewBook:Book):
        self._books.append(NewBook)

    def check_out_book(self ,title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True

    def return_book(self ,title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")
        
"""return_book(self)"""