import pytest
from unittest.mock import patch
from Portfolio_Project.User_Input import get_user_input

def test_user_input():
    user_input = "Test"
    expected = 23
    with patch("builtins.input", return_value = expected) as input_mock:
        actual = get_user_input(user_input)
    input_mock.assert_called()
    assert actual == expected



