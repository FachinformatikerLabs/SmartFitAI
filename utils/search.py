from database.conn import supabase
from kivy.uix.popup import Popup
from kivy.uix.label import Label


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
        result = supabase.table("recipes") \
            .select("instructions", "time") \
            .eq("recipe_id", recipe_id) \
            .execute()
        return {
            'instructions': result.data[0]['instructions'],
            'time': result.data[0]['time']
        }
    
def get_ingredients_details(recipe_id):
    recipe_ingredients = supabase.table("recipe_ingredients") \
        .select("ingredient_id, amount, unit_id") \
        .eq("recipe_id", recipe_id) \
        .execute().data

    ingredients_details = []

    for item in recipe_ingredients:
        ingredient_info = supabase.table("ingredients") \
            .select("ingredient_name, cal_per_unit") \
            .eq("ingredient_id", item['ingredient_id']) \
            .execute().data

        unit_info = supabase.table("units") \
            .select("unit") \
            .eq("unit_id", item['unit_id']) \
            .execute().data

        allergens_info = supabase.table("ingredient_allergens") \
            .select("allergen_id") \
            .eq("ingredient_id", item['ingredient_id']) \
            .execute().data

        allergens = []

        for allergen in allergens_info:
            allergen_name = supabase.table("allergens") \
                .select("allergen_name") \
                .eq("allergen_id", allergen['allergen_id']) \
                .execute().data
            if allergen_name:
                allergens.append(allergen_name[0]['allergen_name'])

        ingredients_details.append({
            "ingredient_name": ingredient_info[0]['ingredient_name'] if ingredient_info else "Zutat nicht gefunden",
            "cal_per_unit": ingredient_info[0]['cal_per_unit'] if ingredient_info else 0,
            "amount": item['amount'],
            "unit": unit_info[0]['unit'] if unit_info else "Einheit nicht gefunden",
            "allergens": allergens
        })

    return ingredients_details