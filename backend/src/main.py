import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"message": "I'm up!"}


@app.get("/config")
async def show_config():
    return {
        "DATABASE_URL": os.environ.get("DATABASE_URL")
    }
