from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    name : str
    writer : str
    price : int
    year : int

class UpdateBook(BaseModel):
    name : Optional[str]
    writer : Optional[str]
    price : Optional[int]
    year : Optional[int]


app = FastAPI()

book_list = []

@app.get("/books")
def get_books():
    return book_list

@app.post("/books", response_model=Book)
def creat_book(book : Book):
    book_list.append(book)
    return book

@app.get("/books/{book_id}")
def get_onebook(book_id : int):
    if book_id - 1 > len(book_list):
        raise HTTPException(status_code=404, detail="없는 책 번호입니다.")
    return book_list[book_id-1]

@app.put("/books/{book_id}")
def update_book(book_id : int, book : UpdateBook):
    if book_id - 1 > len(book_list):
        raise HTTPException(status_code=404, detail="없는 책 번호입니다.")
    coming_book : Book = book_list[book_id-1]
    update_book = book.model_dump(exclude_unset=True)
    updated_book = coming_book.model_copy(update=update_book)
    book_list[book_id-1] = updated_book
    return updated_book

@app.delete("/books/{book_id}")
def delete_book(book_id : int):
    if book_id - 1 > len(book_list):
        raise HTTPException(status_code=404, detail="없는 책 번호입니다.")
    book_list.pop(book_id-1)
    return "책 삭제가 완료되었습니다."
