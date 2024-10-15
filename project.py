class Library:
    def __init__(self, books):
        self.books = books

    def show_available_books(self):
        print("These are the available books in the library")
        for book, borrower in self.books.items():
            if borrower == "free":
                print(book)

    def lend_books(self, requested_book, name):
        requested_book = requested_book.strip().title()

        if requested_book not in self.books:
            print(f"Sorry, {requested_book} is not available in the library.")
            return False
        elif self.books[requested_book] == "free":
            print(f'{requested_book} has been marked as \'Borrowed \' by: {name}')
            self.books[requested_book] = name
            return True
        else:
            print(f'sorry, the {requested_book} is currently not available: {self.books[requested_book]}')
            return False       

    def return_book(self, returned_book):
        returned_book = returned_book.strip().title()
        if returned_book in self.books:
            self.books[returned_book] = "free"
            print(f'{returned_book} has been returned')
        else:
            print(f"Sorry, {returned_book} is not available in the library.")
        

class student:
    def __init__(self, name, library):
        self.name = name
        self.library = library
        self.books = []

    def view_borrowed_books(self):
        if not self.books:
            print(f'{self.name} has not borrowed any books')
        else:
            print(f'{self.name} has borrowed the following books:')
            for book in self.books:
                print(book)

    def request_book(self):
        book = input("Enter the name of the book you\'d like to get OR borrow >>:: ").strip().title()
        
        if self.library.lend_books(book, self.name):
            self.books.append(book)
        

    def return_book(self):
        self.view_borrowed_books()
        book = input("Enter the name of the book you\'d like to return >>:: ").strip().title()
        if book in self.books:
            self.library.return_book(book)
            self.books.remove(book)
            print(f'After returning {book}, the remainig borrowed books are:')
            self.view_borrowed_books()
        else:
            print(f"You don't have {book} in your list of borrowed books Try another...")



def create_mylib():
    books = {
        "Psychology of Money":"free",
        "The Intelligent Investor":"free",
        "Python Coding":"free",
        "The 4-Hour Work Week":"free",
        "Data Science":"free",
        "MachineLearning":"free",
        "The 10X Rule":"free",
        "The 5 AM Club":"free",
        "Java":"free"
    }

    library = Library(books)

    student1 = student("Your name", library)

    while True:
        print("""-------BOOKS AVAILABLE IN LIBRARY-------
              
              1.SHOW AVAILABLE BOOKS
              2.BORROW A BOOK
              3.RETURN A BOOK
              4.VIEW YOUR BOOK
              5.LEAVE FROM THE LIBRARY
              """)
        
        choice = int(input("ENTER YOUR CHOICE:"))

        if choice == 1:
            print()
            library.show_available_books()

        elif choice == 2:
            print()
            student1.request_book()

        elif choice == 3:
            print()
            student1.return_book()

        elif choice == 4:
            print()
            student1.view_borrowed_books()

        elif choice == 5:
            print("Thankyou for using the library Now you can leave")
            exit()

create_mylib()