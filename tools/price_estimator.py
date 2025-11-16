"""PriceEstimator: mock price lookups and basic grouping by aisle."""
class PriceEstimator:
    PRICE_TABLE = {
        'banana': 10,
        'apple': 30,
        'bell pepper': 50,
        'broccoli': 80,
        'milk': 60,
        'eggs': 6
    }

    DEFAULT_AISLE = 'Pantry'

    def optimize(self, grocery_list):
        grouped = {}
        total = 0
        for item in grocery_list:
            name = item['name']
            price = self.PRICE_TABLE.get(name.lower(), 40)
            cost = price * item.get('qty', 1)
            total += cost
            aisle = self._guess_aisle(name)
            if aisle not in grouped:
                grouped[aisle] = []
            grouped[aisle].append({**item, 'est_cost': cost})
        return {'grouped': grouped, 'total_estimated_cost': total}

    def _guess_aisle(self, name):
        ln = name.lower()
        if any(x in ln for x in ['banana', 'apple', 'broccoli', 'pepper']):
            return 'Produce'
        if any(x in ln for x in ['milk', 'eggs']):
            return 'Dairy'
        return self.DEFAULT_AISLE
