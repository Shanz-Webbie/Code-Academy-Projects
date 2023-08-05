import pytest
from unittest.mock import patch
from Portfolio_Project.User_Responses import UserDrivenResponses
from tests.recommendations import get_recommendations

def test_get_recommendations_returns_books():

    responses = UserDrivenResponses(
        GenreFromUser="fiction",
        DoesUserWantFiction= True,
        UserWantsRecentlyPublished= True,
        DoesUserWantStaffRecommendations= True)

    get_recommendations(responses)