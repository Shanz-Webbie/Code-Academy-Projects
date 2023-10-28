from Book import Book
from datetime import datetime


class BookMarshaller:
    def marshall(self, book_dict: dict) -> Book:
        print(book_dict)
        book_details = book_dict["book_details"][0]
        title = book_details['title']
        genre = book_dict["list_name"]
        publish_date = book_dict["published_date"]
        return Book(genre = genre, title = title, publish_date =publish_date)

