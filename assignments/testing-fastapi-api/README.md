# 📘 Assignment: Testing a FastAPI API with pytest

## 🎯 Objective

Write automated tests for the Books API from the FastAPI assignment. Practice using `pytest` and FastAPI's `TestClient` to check that endpoints return the correct status codes and data.

## 📝 Tasks

### 🛠️ Set Up pytest and Write the First Test

#### Description
Install the testing tools with `pip install pytest httpx`. In the same folder as your Books API, create a file named `test_books_api.py`. Write a test that calls the root endpoint and checks the response.

#### Requirements
The completed program must:

- Import the Books API application and create a `TestClient` for it
- Include a test that sends `GET /` and checks for HTTP status `200`
- Check that the response contains the confirmation message from the root endpoint
- Run `pytest` and see the test pass


### 🛠️ Test Creating and Listing Books

#### Description
Write tests that add a book with `POST /books` and then confirm it appears in `GET /books`.

#### Requirements
The completed program must:

- Include a test that sends a valid book to `POST /books` and checks for HTTP status `201`
- Check that the returned book has the `title` and `author` you sent and a generated `id`
- Include a test that sends `GET /books` and checks that the list contains the new book
- Run `pytest` and see all tests pass


### 🛠️ Test Error Cases

#### Description
Write tests that check how the API responds when something goes wrong: a missing book, invalid data, or a deleted book.

#### Requirements
The completed program must:

- Include a test that sends `GET /books/{book_id}` with an ID that does not exist and checks for HTTP status `404`
- Include a test that sends `POST /books` with a missing required field and checks for HTTP status `422`
- Include a test that deletes a book with `DELETE /books/{book_id}`, checks for HTTP status `204`, and then confirms that the same book returns `404`
- Run `pytest` and see all tests pass
