# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing books with FastAPI. Practice defining endpoints, validating request data with Pydantic, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Install FastAPI and Uvicorn with `pip install fastapi uvicorn`, then use the starter code to run an API with `uvicorn starter-code:app --reload`. Create a root endpoint that confirms the Books API is running.

#### Requirements
The completed program must:

- Create a FastAPI application titled `Books API`
- Respond to `GET /` with a JSON message confirming that the API is running
- Start locally with Uvicorn and make the interactive documentation available at `/docs`


### 🛠️ List and Create Books

#### Description
Create a Pydantic model for book data and add endpoints for listing all books and adding a book to the in-memory collection.

#### Requirements
The completed program must:

- Define book input data with required `title` and `author` string fields
- Respond to `GET /books` with the list of books, including an empty list when there are no books
- Accept `POST /books` with a JSON body and add the new book to the collection
- Assign each new book a unique integer `id` and return the created book with HTTP status `201`
- Return a validation error when required fields are missing or have the wrong type


### 🛠️ Retrieve and Delete a Book

#### Description
Add endpoints to retrieve or delete a book by its ID. Handle IDs that do not match any book using the correct HTTP response.

#### Requirements
The completed program must:

- Respond to `GET /books/{book_id}` with the matching book
- Respond to `DELETE /books/{book_id}` by removing the matching book and returning HTTP status `204`
- Return HTTP status `404` when a requested book does not exist
- Verify the create, list, retrieve, and delete workflows using `/docs`