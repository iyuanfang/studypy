from typing import Optional, List

from pydantic import BaseModel

# viewModel里类名为Author
from .book import Book

print("author555555555555555")


class Author(BaseModel):
    id: Optional[int]
    name: str

    books: Optional[List[Book]] = []

    class Config:
        orm_mode = True
