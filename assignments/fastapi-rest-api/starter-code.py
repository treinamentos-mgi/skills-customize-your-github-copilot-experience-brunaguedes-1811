from fastapi import FastAPI

app = FastAPI(title="Books API")


@app.get("/")
def read_root():
    return {"message": "Books API is running"}


# Add your book data model and in-memory collection below.
# Then build the book endpoints described in the assignment.