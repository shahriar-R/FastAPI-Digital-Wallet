import uvicorn
from fastapi import FastAPI

from routers import user, wallet, transaction
from models import wallet as wallet_model, user as user_model, transaction as transaction_model
from db.database import engine

app = FastAPI()

wallet_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)
transaction_model.Base.metadata.create_all(bind=engine)


app.include_router(wallet.router)
app.include_router(user.router)
app.include_router(transaction.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)