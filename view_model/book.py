from typing import Optional

from pydantic import BaseModel


# viewModel里类名为Book
class Book(BaseModel):
    id: Optional[int]
    title: str
    wordNum: int

    class Config:
        orm_mode = True
