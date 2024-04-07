from database.conn import supabase
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import random


def search_recipe(query):
    try:
        recipe_results = supabase.table("recipes") \
            .select("recipe_id, recipe_name, time, instructions, image_url") \
            .ilike("recipe_name", f"%{query}%") \
            .execute()

        recipe_results = recipe_results.data if recipe_results.data else []

        if recipe_results:
            return recipe_results
        popup = Popup(title='Rezept nicht gefunden',
            content=Label(text='Leider wurde kein Rezept mit dem Namen gefunden'), 
            size_hint=(None, None), size=(400, 400))
        popup.open()
        return []

    except Exception as e:

        raise e


def search_ingredient(query):
    try:
        ingredient_results = supabase.table("ingredients") \
            .select("ingredient_id") \
            .ilike("ingredient_name", f"%{query}%") \
            .execute()

        ingredient_ids = [item['ingredient_id'] for item in ingredient_results.data] if ingredient_results.data else []

        if ingredient_ids:
            recipe_ingredient_results = supabase.table("recipe_ingredients") \
                .select("recipe_id") \
                .in_("ingredient_id", ingredient_ids) \
                .execute()
                
            recipe_ids = [item['recipe_id'] for item in recipe_ingredient_results.data] if recipe_ingredient_results.data else []

            if recipe_ids:
                final_recipes = supabase.table("recipes") \
                    .select("*") \
                    .in_("recipe_id", recipe_ids) \
                    .execute()

                return final_recipes.data if final_recipes.data else []
            
        popup = Popup(title='Zutat nicht gefunden',
            content=Label(text=f'Leider wurde kein Rezept mit der Zutat\n{query} gefunden, \nwenn du nach einem Rezept suchst \nverwende bitte die Rezeptsuche'),
            size_hint=(None, None), size=(400, 400))
        popup.open()



        return []

    except Exception as e:
        print(f"Fehler bei der kombinierten Suche: {e}")
        raise e
    

def get_recipe_details(recipe_id):    
    try:
        results = supabase.table("recipe_view") \
            .select("recipe_id, recipe_name, time, instructions, image_url, ingredient_name, amount, unit, allergen_name") \
            .eq("recipe_id", recipe_id) \
            .execute().data
        
        if not results:
            return None

        recipe_details = {
            "recipe_id": results[0]["recipe_id"],
            "recipe_name": results[0]["recipe_name"],
            "time": results[0]["time"],
            "instructions": results[0]["instructions"],
            "image_url": results[0]["image_url"],
            "ingredients": []
        }
        
        ingredients_seen = set()
        for row in results:
            ingredient_key = (row["ingredient_name"], row["amount"], row["unit"])
            if ingredient_key not in ingredients_seen:
                recipe_details["ingredients"].append({
                    "ingredient_name": row["ingredient_name"],
                    "amount": row["amount"],
                    "unit": row["unit"],
                    "allergens": []
                })
                ingredients_seen.add(ingredient_key)
            if row["allergen_name"]:
                for ingredient in recipe_details["ingredients"]:
                    if ingredient["ingredient_name"] == row["ingredient_name"]:
                        ingredient["allergens"].append(row["allergen_name"])
                        break

        return recipe_details
    except Exception as e:
        print(f"Error retrieving recipe details: {e}")
        raise e
    
    
def get_ingredients_details(recipe_id):
    try:
        results = supabase.table("recipe_view") \
            .select("ingredient_name, amount, unit, allergen_name") \
            .eq("recipe_id", recipe_id) \
            .execute().data

        if not results:
            return []

        ingredients_details = {}

        for row in results:

            ingredient_key = (row["ingredient_name"], row["amount"], row["unit"])
            
            if ingredient_key not in ingredients_details:
                ingredients_details[ingredient_key] = {
                    "ingredient_name": row["ingredient_name"],
                    "amount": row["amount"],
                    "unit": row["unit"],
                    "allergens": set()  
                }
            
            if row["allergen_name"]:
                ingredients_details[ingredient_key]["allergens"].add(row["allergen_name"])
        
        ingredients_list = [
            {
                **details, 
                "allergens": list(details["allergens"])
            } for details in ingredients_details.values()
        ]

        return ingredients_list
    except Exception as e:
        print(f"Error retrieving ingredient details: {e}")
        raise e

def get_random_recipe():
    try:
        # Fetch all recipe IDs
        id_response = supabase.table("recipes").select("recipe_id").execute()
        if id_response.data:
            # Choose a random ID
            random_id = random.choice([item['recipe_id'] for item in id_response.data])
            # Fetch the full recipe details including related data
            recipe_query = supabase.table("recipe_view").select("""
                recipe_id,
                recipe_name,
                time,
                instructions,
                image_url,
                calories,
                ingredients:ingredients(ingredient_name, amount, unit, allergens)
            """)
            recipe_result = recipe_query.eq("recipe_id", random_id).execute()
            if recipe_result.data:
                return recipe_result.data[0]
            else:
                print("Failed to retrieve details for random recipe")
                return None
        else:
            print("Failed to fetch recipe IDs")
            return None
    except Exception as e:
        print(f"Error fetching random recipe: {e}")
        return None
