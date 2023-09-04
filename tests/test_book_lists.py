from Portfolio_Project.nytimes import NYTimesApi
import pytest

@pytest.fixture(autouse=True)
def temp_api_key(monkeypatch): #ToDo get token from another place
    monkeypatch.setenv('NYTIMES_API_KEY', ' ')



def test_get_all_list_names_returns_list_of_strings():
    nytimes_api = NYTimesApi(api_key=None)
    actual = nytimes_api.get_all_list_names()
    assert isinstance(actual, list)
    assert len(actual) > 0
    assert all([isinstance(item, str) for item in actual])
