#Dozentenaufgabe überladen und lambdafilter
from utils.search import get_random_recipe

def overload_ingredients():

    #hole mir rezept aus der search via get_random_recipe
    recipe_details = get_random_recipe()

    recipe_id = recipe_details['recipe_id']
    #zieht die rezept infos
    ingredients_details = recipe_details(recipe_id)

    #filter um alles zu auszuwählen dass "a" "e" "i" "o" "u" "ä" "ö" "ü" beinhaltet aber es macht hier absolut garnix weil das alle worte sind
    letter_filter = list(filter(lambda x: all(letter in 'aeiouäöü' for letter in x), ingredients_details))

    # Copy the original recipe details and substitute the ingredients list with the "trolled" one
    overloaded_recipe_details = recipe_details.copy()
    overloaded_recipe_details['ingredients'] = letter_filter

    return overloaded_recipe_details #werden dann in classes überladen