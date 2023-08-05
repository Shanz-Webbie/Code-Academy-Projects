from dataclasses import dataclass
from typing import Optional


@dataclass()
class UserDrivenResponses:
    GenreFromUser: str
    DoesUserWantFiction: bool
    UserWantsRecentlyPublished: bool
    DoesUserWantStaffRecommendations: bool
    UserProvidedThisTitle: Optional[str] = None

