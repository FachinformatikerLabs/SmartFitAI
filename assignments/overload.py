#Dozentenaufgabe Überladen und RegEx
from utils.search import get_random_recipe
import re

def overload_ingredients():

    #hole mir rezept aus der search via get_random_recipe
    recipe_details = get_random_recipe()
    if not recipe_details:
        return None

# TODO: RegEx zur Überprüfung auf Vokale
    regex_pattern = r"[aeiouäöüy]"

    #filtert zutaten die mindestens eins von diesen buchstaben "a" "e" "i" "o" "u" "ä" "ö" "ü" "y" beinhaltet, aber es macht hier absolut garnix weil das alle zutaten sind
    letter_filter = [ing for ing in recipe_details['ingredients'] if re.search(regex_pattern, ing['ingredient_name'], re.IGNORECASE)]

    #kopiert die originalliste der recipedetails und ersetzt die mit der "getrollten" zutaten
    overloaded_recipe_details = recipe_details.copy()
    overloaded_recipe_details['ingredients'] = letter_filter

    return overloaded_recipe_details #werden dann in classes.py überladen