from fastapi import FastAPI
from routes.text import text

app = FastAPI()
app.include_router(text)