import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.user import router as user_router
from .routers.wallet import router as wallet_router
from .routers.transaction import router as transaction_router
from app.models import wallet as wallet_model, user as user_model, transaction as transaction_model
from app.db.database import engine
from .Middlewares import LoggingMiddleware

app = FastAPI()

app.add_middleware(LoggingMiddleware)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allow these origins
    allow_credentials=True,           # Allow cookies to be sent
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers (Authorization, etc.)
)

# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

app.include_router(wallet_router)
app.include_router(user_router)
app.include_router(transaction_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)