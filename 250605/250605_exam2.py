from fastapi import FastAPI



app = FastAPI()

class Book(BaseModel):
    name : str
    writer : str
    price : int
    year : int

book_list = []

@app.get("/books")
def get_books():
    return book_list

@app.post("/books")
def create_books():
    pass





