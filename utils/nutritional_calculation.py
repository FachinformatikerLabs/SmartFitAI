from database.conn import supabase
# Nährwertberechnungslogik mit lambda map
def calculate_total_calories(recipe_id):
    #hole meine zutatenmenge aus supabase
    recipe_ingredients = supabase.table("recipe_ingredients") \
        .select("ingredient_id, amount") \
        .eq("recipe_id", recipe_id) \
        .execute().data

    total_calories = 0
    #hole kalorien pro einheit aus meiner datenbank view
    for ingredient in recipe_ingredients:
        cal_info = supabase.table("ingredients") \
            .select("cal_per_unit") \
            .eq("ingredient_id", ingredient['ingredient_id']) \
            .execute().data

        if cal_info:
# TODO: Lambda Map    
        #nutze die map funktion um meine kalorien pro einheit mit 1 zu multiplizieren könnte man später nutzen "Wieviel Portionen" Abfrage Zutatenmenge zu erhöhen
            n=1
            map_amount = list(map(lambda x: x * n, [ingredient['amount']]))[0]
            total_calories += cal_info[0]['cal_per_unit'] * map_amount

    return total_calories