from Portfolio_Project.Book import Book
from Portfolio_Project.User_Responses import UserDrivenResponses
from Portfolio_Project.recommendations import get_recommendations

def test_get_recommendations_returns_books():

    responses = UserDrivenResponses(
        GenreFromUser="fiction",
        DoesUserWantFiction= True,
        UserWantsRecentlyPublished= True,
        DoesUserWantStaffRecommendations= True)

    actual = get_recommendations(responses)

    assert isinstance(actual, list)
    assert len(actual) > 0
    assert isinstance(actual[0], Book)