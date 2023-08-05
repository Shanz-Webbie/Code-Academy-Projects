from Portfolio_Project.User_Responses import UserDrivenResponses
from Portfolio_Project.BookMarshaller import BookMarshaller
from tests.book_data_source import get_book_data

def get_recommendations(responses: UserDrivenResponses):
    book_marshaller = BookMarshaller()
    book_data = get_book_data()
    actual = book_marshaller.marshall()
