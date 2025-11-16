"""PantryTool: compute missing ingredients by comparing recipes to pantry inventory."""
import copy

def normalize_name(name):
    return name.strip().lower()

class PantryTool:
    def __init__(self):
        pass

    def compute_missing(self, plan_recipes, pantry_items):
        # pantry_items: list of dicts {name, qty, unit}
        pantry_map = {normalize_name(p['name']): p for p in pantry_items}
        missing = {}
        for r in plan_recipes:
            for ing in r.get('ingredients', []):
                n = normalize_name(ing['name'])
                req_qty = ing.get('qty', 1)
                if n in pantry_map:
                    have = pantry_map[n].get('qty', 0)
                    if have >= req_qty:
                        pantry_map[n]['qty'] -= req_qty
                        continue
                    else:
                        missing[n] = missing.get(n, 0) + (req_qty - have)
                        pantry_map[n]['qty'] = 0
                else:
                    missing[n] = missing.get(n, 0) + req_qty
        # return as list of dicts
        return [{'name': k, 'qty': v, 'unit': 'unit'} for k,v in missing.items()]
