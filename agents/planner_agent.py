"""Planner Agent: orchestrates the multi-agent flow for SmartShop."""
from ..tools.recipe_search_tool import RecipeSearchTool
from ..tools.pantry_tool import PantryTool
from ..tools.price_estimator import PriceEstimator
from ..memory.memory_bank import MemoryBank

class PlannerAgent:
    def __init__(self, recipe_tool=None, pantry_tool=None, price_tool=None, memory=None):
        self.recipe_tool = recipe_tool or RecipeSearchTool()
        self.pantry_tool = pantry_tool or PantryTool()
        self.price_tool = price_tool or PriceEstimator()
        self.memory = memory or MemoryBank('memory.json')

    def create_week_plan(self, user_prefs):
        # 1. Search candidate recipes (mocked)
        recipes = self.recipe_tool.search(user_prefs)
        # 2. Score and select recipes
        scored = self._score_recipes(recipes, user_prefs)
        plan = self._select_for_week(scored, days=user_prefs.get('days',7))
        # 3. Compute missing ingredients using pantry tool
        grocery_list = self.pantry_tool.compute_missing(plan, user_prefs.get('pantry',[]))
        # 4. Optimize grocery list for cost and grouping
        optimized = self.price_tool.optimize(grocery_list)
        # 5. Save to memory
        self.memory.save_plan(plan, optimized, user_prefs)
        return {'plan': plan, 'grocery_list': optimized}

    def _score_recipes(self, recipes, prefs):
        # Very simple scoring example: prefer shorter time and budget-friendly
        scored = []
        for r in recipes:
            score = 0
            if r.get('duration_minutes', 60) <= prefs.get('max_time', 45):
                score += 1
            if prefs.get('diet') and prefs['diet'] in r.get('tags', []):
                score += 2
            scored.append((score, r))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [r for s,r in scored]

    def _select_for_week(self, recipes, days=7):
        selected = recipes[:days]
        return selected
