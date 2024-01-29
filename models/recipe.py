# Rezept-Klasse
import nutritional_value

class recipe():

    title = ""                                  #Name des Rezepts
    ingredient = {}                             #Zutaten des Rezepts
    nutrition = nutritional_value               #Nähwert
    preparation_time = 0                        #Zubereitungszeit
    portion_size = 0                            #Portionsgröße
    
    def __init__(self, name, ing, nutri, prep, port, allergen):
        self.title = name
        self.ingredient = ing
        self.nutrition = nutri
        self.preparation_time = prep
        self.portion_size = port
        self.allergens = allergen

    def add_ingredient():
        pass

    def add_recipe():
        pass

    def remove_ingredient():
        pass

    def recipe_details():
        pass

    def calculate_nutrition():
        pass
