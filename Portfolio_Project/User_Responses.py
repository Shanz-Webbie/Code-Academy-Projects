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

    def __init__(self):
        self.GenreFromUser = None
        self.DoesUserWantFiction = False
        self.UserWantsRecentlyPublished = True
        self.DoesUserWantStaffRecommendations = True
        self.UserProvidedThisTitle = None

