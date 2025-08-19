from fastapi import FastAPI
from app.routes import train

app = FastAPI()

app.include_router(train.router, prefix="/train", tags=["train"])