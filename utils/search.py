from database.conn import supabase

def search_combined(query):
    try:
        recipe_results = supabase.table("recipes") \
            .select("recipe_name, time, instructions, image_url") \
            .ilike("recipe_name", f"%{query}%") \
            .execute()

        recipe_results = recipe_results.data if recipe_results.data else []

        if recipe_results:
            return recipe_results

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

        return []

    except Exception as e:
        print(f"Fehler bei der kombinierten Suche: {e}")
        raise e
