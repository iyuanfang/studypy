from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/books/{book_id}")
async def get_book(book_id):
    return {"book_id": book_id}
