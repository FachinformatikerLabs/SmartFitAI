from database.conn import supabase
# Nährwertberechnungslogik
def calculate_total_calories(recipe_id):
    try:
        recipe_ingredients = supabase.table("recipe_ingredients") \
            .select("ingredient_id, amount") \
            .eq("recipe_id", recipe_id) \
            .execute().data

        total_calories = 0

        for ingredient in recipe_ingredients:
            cal_info = supabase.table("ingredients") \
                .select("cal_per_unit") \
                .eq("ingredient_id", ingredient['ingredient_id']) \
                .execute().data

            if cal_info:
                total_calories += cal_info[0]['cal_per_unit'] * ingredient['amount']

        return total_calories
    except Exception as e:
        print(f"Error calculating total calories: {e}")
        raise e