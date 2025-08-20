from fastapi import FastAPI

from app.infrastructure.controllers.guess import guess_controller
from app.infrastructure.controllers.train import train_controller

app = FastAPI()

app.include_router(train_controller.router, prefix="/train", tags=["train"])
app.include_router(guess_controller.router, prefix="/guess", tags=["guess"])