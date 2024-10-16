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

**Clone the repository**:

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

**Generate an SSH Key**
**_ If you want to use an SSH key to secure the database connection (e.g., connecting to a remote PostgreSQL or MySQL server), follow these steps using OpenSSH to generate an SSH key and add it to your environment variables. _**
**Generate the SSH Key**
**_To generate an SSH key using OpenSSH, run the following command in your terminal:_**

```shell
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

- This will generate a private and public SSH key pair.
- Save the private key to a secure location, and copy the public key to the database server where you wish to connect.
- You can name the keys, for example, db_key
  After this, you’ll have two files:
- db_key (Private key)
- db_key.pub (Public key)

**Add the Private Key to the `.env` file**
Now, store the contents of your private key (`db_key`) in the `.env` file. Use the `BASE64` encoding to store the key safely in a single line.
To encode the private key using `base64`, run:

```shell
   cat db_key | base64
```

Copy the output and add it to the .env file as follows:

```
   DB_SSH_KEY="your_base64_encoded_private_key"
```

```shell
    SECRET_KEY="your_secret_key"
    DATABASE_URL="sqlite:///./test.db"

```

**Configure the environment variables**:
Create a .env file to configure your environment variables such as database URL, secret key for JWT tokens, SSH key, etc.
Example `.env` file:

**.env File (Sensitive Environment Variables)**
Here is an example of how your .env file might look:

```shell
   # FastAPI-specific environment variables
   SECRET_KEY="your_secret_key"
   DATABASE_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db/${POSTGRES_DB}"

   # PostgreSQL-specific environment variables
   POSTGRES_USER=your_postgres_user
   POSTGRES_PASSWORD=your_postgres_password
   POSTGRES_DB=your_database_name

   # Base64 encoded SSH private key (for database SSH connections, if applicable)
   DB_SSH_KEY="your_base64_encoded_private_key"
```

**Database Migrations**
**_Migrations are used to manage changes to the database schema over time. This ensures that any updates or modifications to the data models are reflected in the actual database tables without manually altering the database schema._**

**Run the database migrations (\***if using SQLAlchemy**\*)**

```shell
   alembic upgrade head

```

**Run the application**
**_Use Uvicorn to start the FastAPI app._**

```shell
   uvicorn main:app --reload
```

**_The app will be available at http://127.0.0.1:8000._**
