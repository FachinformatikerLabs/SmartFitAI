from database.conn import supabase
# Nährwertberechnungslogik
def calculate_total_calories(recipe_id):
    recipe_ingredients = supabase.table("recipe_ingredients") \
        .select("ingredient_id, amount, unit_id") \
        .eq("recipe_id", recipe_id) \
        .execute().data

    total_calories = 0
    for item in recipe_ingredients:
        ingredient_info = supabase.table("ingredients") \
            .select("cal_per_unit") \
            .eq("ingredient_id", item['ingredient_id']) \
            .execute().data

        if ingredient_info:
            cal_per_unit = ingredient_info[0]['cal_per_unit']
            amount = item['amount']
            total_calories += cal_per_unit * amount

    return total_calories