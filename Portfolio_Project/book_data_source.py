from datetime import datetime

def get_book_data() -> list[dict] :
    publish_date = datetime(year=1937, month=9, day=21)
    book_list = [{"genre": "fiction", "title": "The Hobbit", "publish_date": publish_date}]
    return book_list