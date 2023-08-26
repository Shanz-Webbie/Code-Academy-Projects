from dataclasses import dataclass
from typing import Optional
from Portfolio_Project.User_Input import get_user_input


@dataclass()
class UserDrivenResponses:
    GenreFromUser: str
    DoesUserWantFiction: bool
    UserWantsRecentlyPublished: bool
    DoesUserWantStaffRecommendations: bool
    UserProvidedThisTitle: Optional[str] = None

class UserDrivenResponsesBuilder:
    def build(self) -> UserDrivenResponses:
        new_responses = UserDrivenResponses(

            GenreFromUser= self.GenreFromUser,
            DoesUserWantFiction= self.DoesUserWantFiction,
            UserWantsRecentlyPublished= self.UserWantsRecentlyPublished,
            DoesUserWantStaffRecommendations= self.DoesUserWantStaffRecommendations,
            UserProvidedThisTitle= self.UserProvidedThisTitle
        )

        return new_responses

    def add_genre_from_user(self) -> "UserDrivenResponsesBuilder":
        question = "Which genre of book would you like to read?"
        answer = get_user_input(question)
        self.GenreFromUser = answer

        return self

    def add_does_user_want_fiction(self) -> "UserDrivenResponsesBuilder":
        question = "Would you like to read fiction or nonfiction?"
        answer = get_user_input(question)
        self.DoesUserWantFiction = answer

        return self

    def add_does_user_want_staff_recommendations(self) -> "UserDrivenResponsesBuilder":
        question = "Would you like to read a staff recommended book?"
        answer = get_user_input(question)
        self.DoesUserWantStaffRecommendations = answer

        return self

    def add_does_user_want_recently_published(self) -> "UserDrivenResponsesBuilder":
        question = "Would you like to read a recently published book?"
        answer = get_user_input(question)
        self.DoesUserWantFiction = answer

        return self


    def add_does_user_know_the_book_title(self) -> "UserDrivenResponsesBuilder":
        question = "Is there a specific book title that you are looking for?"
        answer = get_user_input(question)
        self.UserProvidedThisTitle = answer

        return self

    def __init__(self):
        self.GenreFromUser = None
        self.DoesUserWantFiction = False
        self.UserWantsRecentlyPublished = True
        self.DoesUserWantStaffRecommendations = True
        self.UserProvidedThisTitle = None

