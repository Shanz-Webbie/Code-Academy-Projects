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

    def get_list_of_books(self, list_id, bestsellers_date=None, published_date=None, offset=None):
        url = f'https://api.nytimes.com/svc/books/v3/lists.json?api-key={self.api_key}'
        params = {'list': list_id}
        if bestsellers_date is not None:
            pass
        if published_date is not None:
            pass
        if offset is not None:
            pass
        response = requests.get(url, params=params)
        return response.json()

    def get_all_list_names(self) -> list[str]:
        nytimes_lists_response_dict =  self.get_nytimes_lists()
        list_of_names = []
        for item in nytimes_lists_response_dict['results']:
            encoded_list = item['list_name_encoded']
            list_of_names.append(encoded_list)
        return list_of_names




def main():
    nytimes_api = NYTimesApi(api_key=None)
    lists_json = nytimes_api.get_nytimes_lists()
    lists_books = nytimes_api.get_list_of_books(list_id='hardcover-fiction')
    print(lists_json)
    #print(lists_books)

if __name__ == '__main__':
    main()

