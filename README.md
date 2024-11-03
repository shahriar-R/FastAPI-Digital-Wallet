# FastAPI ToDoApp

This is a **To-Do Application** built using **FastAPI**, a modern, fast web framework for building APIs with Python 3.7+.

The app allows users to create, read, update, and delete tasks (CRUD operations) and includes features like user authentication and basic task management. The backend is built with FastAPI, while it can be easily extended to integrate with any frontend framework like React.

## Features

- FastAPI for the backend
- PostgreSQL for the database
- Docker for containerization
- Nginx for reverse proxy and `ssl` certificate
- **User Authentication**: Secure authentication for user accounts.
- **CRUD Operations**: Users can create, read, update, and delete tasks.
- **Task Management**: Allows users to manage their to-do lists efficiently.
- **Fast and Lightweight**: Powered by FastAPI, which ensures high performance.
- **Asynchronous Support**: FastAPI’s asynchronous nature helps handle multiple requests seamlessly.

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: PostgreSQL (or replaceable with  MySQL, etc.)
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

**Run Alembic migrations**
**Database Migrations**
Migrations are used to manage changes to the database schema over time. This ensures that any updates or modifications to the data models are reflected in the actual database tables without manually altering the database schema.
```shell
   alembic upgrade head

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

***1-SSL Certificate and Key:***
 - ssl_certificate /etc/ssl/your_certificate.crt;
 - ssl_certificate_key /etc/ssl/your_private.key;
These lines specify the paths to your SSL certificate and private key. Make sure these files are correctly placed at these paths.
```
openssl genpkey -algorithm RSA -out /etc/ssl/private/your_private.key
openssl req -new -key /etc/ssl/private/your_private.key -out /etc/ssl/csr/your_request.csr
openssl x509 -req -days 365 -in /etc/ssl/csr/your_request.csr -signkey /etc/ssl/private/your_private.key -out /etc/ssl/certs/your_certificate.crt

```
copy your_private.key to nginx/ssl/private.key and your_certificate.crt to nginx/ssl/certificate.crt
**Nginx Configuration with SSL for FastAPI**
This configuration sets up Nginx as a reverse proxy for a FastAPI application, handling both HTTP and HTTPS traffic. It redirects all HTTP traffic to HTTPS and uses a provided SSL certificate and key to secure the communication.

***HTTP to HTTPS Redirect***
The first server block listens on port 80 (HTTP) and redirects all incoming traffic to the corresponding HTTPS URL:The first server block listens on port 80 (HTTP) and redirects all incoming traffic to the corresponding HTTPS URL:
```
server {
    listen 80;
    server_name localhost;
    return 301 https://$host$request_uri;
}
```
***HTTPS Server Block***
The second server block listens on port 443 (HTTPS) and uses the provided SSL certificate and key to secure the communication:
```
server {
    listen 443 ssl;
    server_name localhost;

    ssl_certificate /etc/ssl/your_certificate.crt;
    ssl_certificate_key /etc/ssl/your_private.key;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    location / {
        proxy_pass http://app:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
***2-Logs:***
 - access_log /var/log/nginx/access.log;
 - error_log /var/log/nginx/error.log;
These lines specify where the access and error logs are stored.
***3-Location Block:***
 - location / { ... }

 - This block proxies all requests to your FastAPI application running on http://app:8000. The proxy_set_header directives ensure that the correct headers are passed to the backend, maintaining the client information and protocol.

 **How to Apply This Configuration**
  - Place your SSL certificate and key in the specified paths (e.g., /etc/ssl/your_certificate.crt and /etc/ssl/your_private.key).

 - Copy the Nginx configuration to the appropriate directory (e.g., /etc/nginx/sites-available/your_config).

- Create a symbolic link to the sites-enabled directory:
```
  sudo ln -s /etc/nginx/sites-available/your_config /etc/nginx/sites-enabled/
```
 - Test the Nginx configuration to ensure there are no syntax errors:
 ```
 sudo nginx -t
```

**Build and run the containers**

```shell
   docker-compose up --build
```

**Access the application**
The application will be available at `http://localhost:8000`. You can also access the automatic interactive API documentation at `http://localhost:8000/docs` or `http://localhost:8000/redoc`.


