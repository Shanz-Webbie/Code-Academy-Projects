from Book import book

def greet():
    print("Hi there and welcome to the book recommendation library!\n"")
    print("We'll help you find the perfect book to read next")

def get_genre(book, genre):
    book_genre = input("Would you like to read a fiction or nonfiction book?")
    if book_genre == "fiction":
        print("Please select one of the following genres:")
    elif book_genre == "nonfiction":
        print("Please select one of the following genres:")
    else:
        print("Please select a fiction or nonfiction book.")
