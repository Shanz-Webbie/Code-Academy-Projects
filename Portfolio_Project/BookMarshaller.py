from .Book import Book
from datetime import datetime


class BookMarshaller:
    def marshall(self, book_dict: dict) -> Book:
        genre = book_dict["genre"]
        title = book_dict["title"]
        publish_date = book_dict["publish_date"]
        return Book(genre = genre, title = title, publish_date =publish_date)

