from fastapi import APIRouter
import os
import requests
from typing import List
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY_1") 

router = APIRouter()

@router.get("/")
def root():
    return {"message" : "Welcome to Cookit API!"}

@router.get("/recipeByIngredients")
def get_recipe_by_ingredients(ingredients, number=1):
    URL = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        'apiKey': API_KEY,
        'ingredients':ingredients,
        'number': number,
        'ranking': 1
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    return response.json()
