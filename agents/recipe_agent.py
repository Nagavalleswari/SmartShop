"""Recipe Research Agent: mocked search over local recipe dataset."""
import json, os
from pathlib import Path

RECIPES_PATH = Path(__file__).parents[2] / 'data' / 'recipes.json'

class RecipeAgent:
    def __init__(self, recipe_path=None):
        self.recipe_path = recipe_path or RECIPES_PATH

    def list_all(self):
        with open(self.recipe_path, 'r') as f:
            return json.load(f)

    def search(self, prefs):
        # Very simple filter based on diet and excluded ingredients
        all_recipes = self.list_all()
        out = []
        for r in all_recipes:
            if prefs.get('diet') and prefs['diet'] not in r.get('tags', []):
                continue
            excluded = prefs.get('exclude', [])
            if any(e.lower() in ','.join([ing['name'].lower() for ing in r['ingredients']]) for e in excluded):
                continue
            out.append(r)
        return out
