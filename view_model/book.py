from typing import Optional

from pydantic import BaseModel

# viewModel里类名为Book

print("book555555555555555")


class Book(BaseModel):
    id: Optional[int]
    title: str
    wordNum: int

    author_id: int

    class Config:
        orm_mode = True
