import random
from utils.search import get_recipe_details, get_ingredients_details
from database.conn import supabase

def get_random_recipe():
    id_response = supabase.table("recipes").select("recipe_id").execute()
    if id_response.data:

        random_id = random.choice([item['recipe_id'] for item in id_response.data])
        return get_recipe_details(random_id)
    else:
        print("Failed to fetch recipe IDs")
        return None

def get_shuffled_ingredients_recipe():
    recipe_details = get_random_recipe()
    if not recipe_details:
        print("No recipe found")
        return None, None

    recipe_id = recipe_details['recipe_id']
    ingredients_details = get_ingredients_details(recipe_id)

    random.shuffle(ingredients_details)
    return recipe_details, ingredients_details

def overload_with_shuffled_ingredients():
    from utils.classes import RecipeDetails 
    
    recipe_details = get_random_recipe()
    if not recipe_details:
        print("No recipe found")
        return None

    recipe_id = recipe_details['recipe_id']
    ingredients_details = RecipeDetails(recipe_id).get_ingredients_details()

    random.shuffle(ingredients_details)
    overloaded_recipe_details = recipe_details.copy()
    overloaded_recipe_details['ingredients'] = ingredients_details

    return overloaded_recipe_details