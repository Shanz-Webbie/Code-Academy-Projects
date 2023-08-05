from Portfolio_Project.Book import Book
from Portfolio_Project.User_Responses import UserDrivenResponses
from Portfolio_Project.BookMarshaller import BookMarshaller
from Portfolio_Project.book_data_source import get_book_data

def get_recommendations(responses: UserDrivenResponses) -> list[Book]:
    book_marshaller = BookMarshaller()
    book_data = get_book_data()
    list_of_books = []
    for book_dict in book_data:
        book_object = book_marshaller.marshall(book_dict)
        list_of_books.append(book_object)
    return list_of_books