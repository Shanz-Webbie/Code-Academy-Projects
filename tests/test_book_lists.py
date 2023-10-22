from Portfolio_Project.nytimes import NYTimesBookRepositoryAdapter
import pytest


def get_api_key_filepath():
    return "/Users/shanz/PycharmProjects/Code-Academy/.api_key"


def get_api_key():
    with open(get_api_key_filepath()) as api_key_file:
        return api_key_file.read()


@pytest.fixture(autouse=True)
def fake_api_key(monkeypatch):
    monkeypatch.setenv('NYTIMES_API_KEY', get_api_key())

@pytest.fixture
def subject():
    test_subject = NYTimesBookRepositoryAdapter(api_key=None)
    yield test_subject


def test_get_all_list_names_returns_list_of_strings(subject):
    actual = subject.get_all_genres()
    assert isinstance(actual, list)
    assert len(actual) > 0
    assert all([isinstance(item, str) for item in actual])


def test_get_list_of_books_returns_a_list_of_dictionaries(subject):
    list_id = "hardcover-fiction"
    actual = subject.get_list_of_books(list_id)
    assert isinstance(actual, list)
    assert len(actual) > 0
    assert all([isinstance(item, dict) for item in actual])
