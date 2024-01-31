# Zutat-Klasse

class ingredient():
    
    ingredient = ""             # Name der Zutat
    quantity = 0.0              # Menge
    unit = ""                   # Einheit
    category = ""               # Kategorie der Zutat
    allergens = ""              # Allergene

    def __init__(self, ing, quan, unit, cat, allerg):
        self.ingredient = ing
        self.quantity = quan
        self.unit = unit
        self.category = cat
        self.allergens = allerg

    
    def show():                 # Informationen anzeigen lassen
        pass

    def raise_quan():           # Menge erhöhen
        pass

    def reduce_quan():          # Menge verringern
        pass