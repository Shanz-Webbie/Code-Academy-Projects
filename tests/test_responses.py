from Portfolio_Project.User_Responses import UserDrivenResponsesBuilder, UserDrivenResponses
from unittest.mock import patch

def test_builder_builds_userdrivenresponses():
    Builder = UserDrivenResponsesBuilder()

    actual = Builder.build()
    assert isinstance(actual,UserDrivenResponses)

def test_add_genre_from_user_returns_builder():
    Builder = UserDrivenResponsesBuilder()
    example_genre = "Fantasy"
    with patch("Portfolio_Project.User_Responses.get_user_input", return_value=example_genre) as input_mock:
        actual = Builder.add_genre_from_user()
    input_mock.assert_called()
    assert isinstance(actual, UserDrivenResponsesBuilder)
    assert Builder.GenreFromUser is not None
    assert Builder.GenreFromUser == example_genre
