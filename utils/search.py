from database.conn import supabase

def search_recipes(query):
    try:
        result = supabase.table("recipes") \
            .select("recipe_name, time, instructions, image_url") \
            .ilike("recipe_name", f"%{query}%") \
            .execute()

        if result.data:
            return result.data
        else:
            print("Keine Rezepte gefunden, die dem Suchbegriff entsprechen.")
            return []
    except Exception as e:
        print(f"Fehler bei der Suche nach Rezepten: {e}")
        raise e
