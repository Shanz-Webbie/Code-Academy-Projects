import requests
import os


class NYTimesApi:
    def __init__(self, api_key = None):
        if api_key is None:
            api_key = os.getenv('NYTIMES_API_KEY')
        self.api_key = api_key

    def get_nytimes_lists(self):
        url = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={self.api_key}'
        response = requests.get(url)
        return response.json()


def main():
    nytimes_api = NYTimesApi(api_key=None)
    lists_json = nytimes_api.get_nytimes_lists()
    print(lists_json)


if __name__ == '__main__':
    main()
