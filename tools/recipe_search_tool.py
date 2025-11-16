"""RecipeSearchTool: adapter that uses RecipeAgent to expose a tool-like interface."""
from ..agents.recipe_agent import RecipeAgent

class RecipeSearchTool:
    def __init__(self, agent=None):
        self.agent = agent or RecipeAgent()

    def search(self, prefs):
        return self.agent.search(prefs)
