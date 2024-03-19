from database.conn import supabase

#Die ID der eingegeben Zutat suchen
def search_ingredient_id(self):
    search_recipe = self.ids.search_recipe.text
    try: 
        search_data = supabase.table("ingredients").select("ingredient_id").eq("ingredient_name", search_recipe).execute()
        ing_id=search_data.data[0]["ingredient_id"]
        search_recipe_id(ing_id)
    except: 
        print("Die Zuatat existiert leider nicht")   #-> Popup erstellen, dass auf den Fehler hinweist

#Alle für die Zutat (über die ID geprüft) verfügbaren Rezept-IDs anzeigen
def search_recipe_id(ing_id):
    try:
        search_rec = supabase.table("recipe_ingredients").select("recipe_id").eq("ingredient_id", ing_id).execute()
        rec_ids = [item["recipe_id"] for item in search_rec.data]
        search_recipe_name(rec_ids)
    except:
        print("Zu der Gewählten Zutat existiert kein Rezept")   #-> Popup erstellen, dass auf den Fehler hinweist

#Den Rezeptnamen zu den Rezept IDs suchen
def search_recipe_name(rec_ids):
    recipes = supabase.table("recipes").select("recipe_name").in_("recipe_id", rec_ids).execute()
    rec_name=[recipe["recipe_name"] for recipe in recipes.data]
    search_recipe_image(rec_name)

#Das Bild zu dem Rezeptnamen raussuchen
def search_recipe_image(rec_name):
    try:
        for recipe in rec_name:
            recipe_image = supabase.table("recipes").select("image_url").in_("recipe_name", rec_name).execute()
            print(recipe_image)
        for recipe in rec_name:
            print(recipe)
    except:
        print("Kein Bild gefunden") 
#-> Das Bild mit dem Namen sollen in Fenstern erscheinen, die man dann drücken kann, um zu dem Rezept 
# und der Zubereitung zu gelangen.