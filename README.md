# FastAPI ToDoApp

This is a **To-Do Application** built using **FastAPI**, a modern, fast web framework for building APIs with Python 3.7+.

The app allows users to create, read, update, and delete tasks (CRUD operations) and includes features like user authentication and basic task management. The backend is built with FastAPI, while it can be easily extended to integrate with any frontend framework like React.

## Features

- **User Authentication**: Secure authentication for user accounts.
- **CRUD Operations**: Users can create, read, update, and delete tasks.
- **Task Management**: Allows users to manage their to-do lists efficiently.
- **Fast and Lightweight**: Powered by FastAPI, which ensures high performance.
- **Asynchronous Support**: FastAPI’s asynchronous nature helps handle multiple requests seamlessly.

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: SQLite (or replaceable with PostgreSQL, MySQL, etc.)
- **Authentication**: JWT (JSON Web Tokens)
- **Dependencies Management**: `pip` and `virtualenv`

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Uvicorn (for running the ASGI server)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/shahriar-R/FastAPI-ToDoApp.git
   cd FastAPI-ToDoApp
   ```

**Create virtual environment**:

```shell
   python3 -m venv venv

```

```shell
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Install dependencies**:

```shell
  pip install -r requirements.txt
```

**Configure the environment variables**:
**_Create a .env file to configure your environment variables such as database URL, secret key for JWT tokens, etc._**

```shell
    SECRET_KEY="your_secret_key"
    DATABASE_URL="sqlite:///./test.db"

```

**Run the database migrations (\***if using SQLAlchemy**\*)**

```shell
   alembic upgrade head

```

**_The app will be available at http://127.0.0.1:8000._**

**Run the application**
**_Use Uvicorn to start the FastAPI app._**

```shell
   uvicorn main:app --reload
```
