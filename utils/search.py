from database.conn import supabase
from kivy.uix.popup import Popup
from kivy.uix.label import Label


def search_recipe(query):
    try:
        recipe_results = supabase.table("recipes") \
            .select("recipe_name, time, instructions, image_url") \
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
    

