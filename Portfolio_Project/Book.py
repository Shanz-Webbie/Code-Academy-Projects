from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Book:
    title: str
    genre: str
    publish_date: datetime


