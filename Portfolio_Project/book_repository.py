from abc import ABC, abstractmethod


class AbstractBookRepository(ABC):

    @abstractmethod
    def get_all_genres(self) -> list[str]:
        pass