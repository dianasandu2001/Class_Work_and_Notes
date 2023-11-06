#outcome:
#Author: J.K. rowling
#Books written by the author:
#- Harry Potter and the Sorcerer's Stone
#- I don't know
#
#Author: George Orwell
#Books written by the author:
#- the year 1984
#
#The author of '1984' is George Orwell

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_author_name(self):
        return self.author.name

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

#Author("J.K. Rowling").add_book(Book("Harry Potter and the Sorcerer's Stone", author1))
#Author("J.K. Rowling").add_book(Book("I donot know", author1))
#Author("George Orwell").add_book(Book("The year 1984", author2))

#This is easier to read
author1 = Author("J.K. Rowling")
author2 = Author("George Orwell")

book1 = Book("Harry Potter and the Sorcerer's Stone", author1)
book2 = Book("The year 1984", author2)
book3 = Book("I don't know", author1)

author1.add_book(book1)
author1.add_book(book3)
author2.add_book(book2)

for author in [author1, author2]:
    print(f"Author: {author.name}")
    print("Books written by the author: ")
    for book in author.books:
        print(f"- {book.title}")
    print()

#Get the author of a book
print(f"The author of 'The year 1984' is {book2.get_author_name()}")