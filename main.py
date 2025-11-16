"""Demo runner for SmartShop skeleton."""
from smartshop.agents.planner_agent import PlannerAgent
from smartshop.tools.recipe_search_tool import RecipeSearchTool

def sample_user_prefs():
    return {
        'diet': 'vegetarian',
        'exclude': ['peanuts','cilantro'],
        'max_time': 45,
        'days': 7,
        'pantry': [
            {'name':'eggs','qty':6},
            {'name':'milk','qty':1}
        ]
    }

def main():
    planner = PlannerAgent()
    prefs = sample_user_prefs()
    result = planner.create_week_plan(prefs)
    print('--- Generated Plan ---')
    for i, r in enumerate(result['plan'],1):
        print(f"{i}. {r.get('title')}")
    print('\n--- Grocery List ---')
    print(result['grocery_list'])

if __name__ == '__main__':
    main()
