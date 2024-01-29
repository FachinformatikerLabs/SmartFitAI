# Nährwertberechnungslogik
class Recipe:
    def __init__(self):
        self.ingredients = {}  #dictionary um die zutaten und zutatenmenge zu speichern
    
    def calculate_calories(self):
        total_calories = 0 #initialisiert gesmamten kalorien als variable
        for ingredient, amount in self.ingredients.items(): #für jede zutat und menge aus dem ingredients dictionary
            total_calories += ingredient.calories * amount  #addiert gesamt kaolirien mit der (kalorien einer zutat * menge)
        return total_calories 