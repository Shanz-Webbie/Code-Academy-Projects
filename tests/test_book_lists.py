from Portfolio_Project.nytimes import NYTimesApi
import pytest


@pytest.fixture(autouse=True)
def fake_api_key(monkeypatch): #ToDo get token from another place
    monkeypatch.setenv('NYTIMES_API_KEY', '')

@pytest.fixture
def subject():
    test_subject = NYTimesApi(api_key=None)
    yield test_subject


def test_get_all_list_names_returns_list_of_strings(subject):
    actual = subject.get_all_list_names()
    assert isinstance(actual, list)
    assert len(actual) > 0
    assert all([isinstance(item, str) for item in actual])


def test_get_list_of_books_returns_a_list_of_dictionaries(subject):
    list_id = "hardcover-fiction"
    actual = subject.get_list_of_books(list_id)
    assert isinstance(actual, list)
    assert len(actual) > 0
    assert all([isinstance(item, dict) for item in actual])
