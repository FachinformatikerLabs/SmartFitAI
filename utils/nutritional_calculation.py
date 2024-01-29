# Nährwertberechnungslogik

def calculate_calories(self):
    total_calories = 0
    for ingredient, amount in self.ingredients.items():
        total_calories += ingredient.calories * amount  
    return total_calories