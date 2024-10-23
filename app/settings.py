import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class Settings:

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    DATABASE_URL =f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    print(load_dotenv(dotenv_path="./.env"))
    print(f"POSTGRES_PASSWORD={POSTGRES_PASSWORD}")
    print(f"POSTGRES_DB={POSTGRES_DB}")
    print(f"POSTGRES_PORT={POSTGRES_PORT}")
    print(f"POSTGRES_HOST={POSTGRES_HOST}")

    if not all([POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_PORT, POSTGRES_HOST]):
        raise ValueError("One or more environment variables are not set")
setting = Settings()