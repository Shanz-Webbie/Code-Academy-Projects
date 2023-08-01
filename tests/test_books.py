import pytest
from datetime import datetime
from Portfolio_Project.Book import Book
from Portfolio_Project.BookMarshaller import BookMarshaller


def test_book_constructor_creates_valid_book():
    publish_date = datetime(year= 1937, month= 9, day= 21 )
    new_book = Book(genre = "fiction", title = "The Hobbit", publish_date = publish_date)
    assert isinstance(new_book, Book)
    assert new_book.title == "The Hobbit"

def test_dict_to_book_marshalling_works():
    publish_date = datetime(year=1937, month=9, day=21)
    hobbit_dict = {"genre": "fiction", "title": "The Hobbit", "publish_date": publish_date}
    book_marshaller = BookMarshaller()
    actual = book_marshaller.marshall(hobbit_dict)
    assert isinstance(actual, Book)


