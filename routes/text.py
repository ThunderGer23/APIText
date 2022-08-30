from fastapi import APIRouter

text = APIRouter()

@text.get('/')
def home():
    return 'This route from analize the docs with IA'