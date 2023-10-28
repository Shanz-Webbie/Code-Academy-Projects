from abc import ABC, abstractmethod
from Book import Book


class AbstractBookRepository(ABC):

    @abstractmethod
    def get_all_genres(self) -> list[str]:
        pass

    @abstractmethod
    def get_books_for_genre(self, genre: str) -> list[Book]:
        pass





