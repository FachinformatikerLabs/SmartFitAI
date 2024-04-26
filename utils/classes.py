from utils.imports import *

load_dotenv()
DEV_MODE = os.getenv('DEV_MODE') == 'True'

class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()
    icon = StringProperty()

#Definieren der verschiedenen Screens:
class Login(MDScreen):
   def login_user(self):
      if DEV_MODE:
          print("Entwicklungsmodus aktiv - Login übersprungen")
          self.manager.current = "Dashboard"
          return

      email = self.ids.email.text
      password = self.ids.password.text

      user_data = supabase.table("user_profiles").select("*").eq("email", email).execute()
      
      if user_data.data:
         stored_password = user_data.data[0]["password"]

         if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            self.manager.current = "Dashboard"
         else: 
            print("Falsches Passwort")
      else:
         print("Benutzer wurde nicht gefunden")

class CreateUser(MDScreen):

    def register_user(self):
        user_name = self.ids.user_name.text
        email = self.ids.email.text
        password = self.ids.password.text
        birthday = self.ids.birthday.text

        # Hier hashen wir das Passwort mit bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        #das geburtsdatum wird als dd.mm.yyyy eingegeben und dann für die SQL db in mm.dd.yyyy umgewandelt
        birthday_dmy = datetime.strptime(birthday, "%d.%m.%Y")
        birthday_SQL = birthday_dmy.strftime("%m.%d.%Y")

        # Hier erstellen wir den Benutzer
        data = {
            "user_name": user_name,
            "email": email,
            "password": hashed_password,
            "birthday": birthday_SQL,
        }

        # Führe die Datenbankeinfügung aus und prüfe auf Erfolg
        error = supabase.table("user_profiles").insert(data).execute()

        # Ohne Fehler geht's zum dashboard, macht zwar wenig Sinn aber machen wir mal so
        if not error:
            self.manager.current = 'Dashboard'
        else:
            print(f"Registrierung fehlgeschlagen für {email}: {error}")

        print(f"Versuch der Registrierung für {email} abgeschlossen.")

    def checkbox_click(self, instances, value):
        if value == True:
            pass
        else:
            pass

class RecipeDetails:
# TODO: Annotation: Rezept ID als Integer und Gesamtkalorien als Fließkommazahl
    def __init__(self, recipe_id: int): #annotation: Typen-Hinweis integer
        self.recipe_id = recipe_id
    
    def get_total_calories(self) -> float: #annotation: Typen-Hinweis float
        return calculate_total_calories(self.recipe_id)
    
    def get_recipe_details(self):    
        return get_recipe_details(self.recipe_id)

class SearchResultCard(MDCard):
    def __init__(self, recipe_id, recipe_name, image_url, **kwargs):
        super().__init__(**kwargs)
        self.recipe_id = recipe_id
        self.size_hint = None, None
        self.size = "240dp", "240dp"
        self.orientation = "vertical"

        # Bild
        self.add_widget(AsyncImage(
            source=image_url,
            size_hint_y=None,
            height="140dp"
        ))

        # Name des Rezepts
        self.add_widget(MDLabel(
            text=recipe_name,
            halign="center"
        ))

    def on_release(self):
        app = MDApp.get_running_app()
        app.switch_screen('Recipe')
        recipe_screen = app.root.get_screen('Recipe')
        recipe_screen.display_recipe_details(self.recipe_id)

class SearchBar(BoxLayout):
    def on_search(self, query: str) -> None: #annotation: Typen-Hinweis string
        app = MDApp.get_running_app()
        results = search_ingredient(query) 
        if results:
            app.root.current = 'Search'
            search_screen = app.root.get_screen('Search')
            search_screen.display_results(results)

class Search(MDScreen):
    def display_results(self, results):
        self.ids.results_grid.clear_widgets()
        for result in results:
            card = SearchResultCard(recipe_id=result['recipe_id'], recipe_name=result['recipe_name'], image_url=result['image_url'])
            card.bind(on_release=lambda instance, x=result['recipe_id']: self.open_recipe_details(x))
            self.ids.results_grid.add_widget(card)

    def open_recipe_details(self, recipe_id):
        app = MDApp.get_running_app()
        app.switch_screen('Recipe')
        recipe_screen = app.root.get_screen('Recipe')
        recipe_screen.display_recipe_details(recipe_id)

#rezept des tages
class RecipeOfTheDayScreen(MDScreen):
    def on_pre_enter(self):
        #recipe of the day laden 
        self.display_recipeoftheday()

    def display_recipeoftheday(self):
        #daten aus dem singleton holen
        recipe_details = RecipeOfTheDay.get_recipe_of_the_day()
        if recipe_details:
            self.update_recipe_details(recipe_details)
        else:
            print("Rezeptdetails konnten nicht geladen werden")

    def update_recipe_details(self, recipe_details):
        #Rezeptdetails aktualisieren
        self.ids.recipe_image.source = recipe_details.get('image_url', 'default_image.jpg')
        self.ids.name_label.text = f"Rezeptname: {recipe_details.get('recipe_name', 'Unbekanntes Rezept')}"
        self.ids.time_label.text = f"Zubereitungszeit: {recipe_details.get('time', 'Unbekannte Zeit')} Minuten"
        self.ids.calories_label.text = f"Gesamtkalorien: {calculate_total_calories(recipe_details.get('recipe_id', None))}"
        self.ids.instructions_label.text = f"Anweisungen: {recipe_details.get('instructions', 'Keine Anweisungen verfügbar')}"

        #Listen für Zutaten und Allergene hier
        ingredient_lines = [f"{ing['ingredient_name']}: {ing['amount']} {ing['unit']}" for ing in recipe_details.get('ingredients', [])]
        allergens_set = {allergen for ing in recipe_details.get('ingredients', []) for allergen in ing.get('allergens', [])}

        self.ids.ingredients_label.text = "Zutaten:\n" + "\n".join(ingredient_lines)
        self.ids.allergens_label.text = "Enthaltene Allergene: " + ', '.join(allergens_set)
        self.ids.special_message_label.text = recipe_details.get('special_message', 'Heute ist ein ganz normaler Tag.') #Wenn tag in Liste eingetragen gibt er speziellen Text aus


#rezeptseite 
class Recipe(MDScreen):
    def display_recipe_details(self, recipe_id):
        recipe_details = RecipeDetails(recipe_id).get_recipe_details()
        if recipe_details:
            self.ids.recipe_image.source = recipe_details['image_url']
            self.ids.name_label.text = f"Rezeptname: {recipe_details['recipe_name']}"
            self.ids.time_label.text = f"Zubereitungszeit: {recipe_details['time']} Minuten"
            self.ids.calories_label.text = f"Gesamtkalorien: {calculate_total_calories(recipe_id)}"
            self.ids.instructions_label.text = f"Anweisungen: {recipe_details['instructions']}"
            
            ingredient_lines = [f"{ing['ingredient_name']}: {ing['amount']} {ing['unit']}" for ing in recipe_details['ingredients']]
            allergens_set = {allergen for ing in recipe_details['ingredients'] for allergen in ing['allergens']}
            
            self.ids.ingredients_label.text = "Zutaten:\n" + "\n".join(ingredient_lines)
            self.ids.allergens_label.text = "Enthaltene Allergene: " + ', '.join(allergens_set)
        else:
            print("Details for the recipe not found")

#zufallsrezept         
    def on_pre_enter(self):
        recipe_details = get_random_recipe()
        if recipe_details:
            self.display_recipe_details(recipe_details['recipe_id'])
        else:
            print("No recipe details available")

# TODO: Überladen: Rezeptzutaten von einer ID wird mit den RegEx gefilterten Zutaten aus dem gleichen rezept aus der overload.py überladen
    def load_overloaded_random_recipe(self):
        overloaded_details = overload_ingredients()
        if overloaded_details:
            self.display_recipe_details(overloaded_details['recipe_id'])
        else:
            print("Failed to load overloaded recipe")
            
#rekursiver countdown wenn zurück button gedrückt wird
    def go_back_with_countdown(self):
        print("Starte Countdown...")
        countdown(3)
        print("Wechsel zur Suchseite...")
        self.manager.current = 'Search'

class Construction(MDScreen):
    pass
  
class SearchPopup(Popup):
    def on_search_pop(self, query):
        app = MDApp.get_running_app()
        results = search_recipe(query) 
        if results:
            app.root.current = 'Search'
            search_screen = app.root.get_screen('Search')
            search_screen.display_results(results)


class NavLayout(BoxLayout):
    pass
 
class BackgroundLayout(Image):
    pass

class Dashboard(MDScreen):
    pass

class Profil(MDScreen):
   pass


class WindowManager(ScreenManager):
   pass

class SmartFitAIApp(MDApp):
    def switch_screen(self, screen_name):
        self.root.current = screen_name

    def show_popup(self):

        popup = SearchPopup()
        popup.open()
        print("geht")

    def build(self):
        self.supabase = supabase
        inspector.create_inspector(Window, self)

        # Laden der verschiedenen .kv Design Files
        Builder.load_file("pages/recipe.kv", encoding="utf8")
        Builder.load_file("pages/login.kv", encoding="utf8")
        Builder.load_file("pages/registration.kv", encoding="utf8")
        Builder.load_file("pages/dashboard.kv", encoding="utf8")
        Builder.load_file("pages/search.kv", encoding="utf8")
        Builder.load_file("pages/profil.kv", encoding="utf8")
        Builder.load_file("pages/construction.kv", encoding="utf8")
        Builder.load_file("pages/recipeoftheday.kv", encoding="utf8")
        Builder.load_file("components/nav.kv", encoding="utf8")
        Builder.load_file("components/searchbar.kv", encoding="utf8")
        Builder.load_file("components/background.kv", encoding="utf8")
        Builder.load_file("components/searchpopup.kv", encoding="utf8")


        # Definition verschiedener Layouts (Aktuell nur "Darkmode")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Darkblue" 

        Window.size = (1200,700)

        # Initialisiere den ScreenManager und füge die Screens hinzu
        sm = WindowManager()
        sm.add_widget(Login(name='Login'))
        sm.add_widget(CreateUser(name='NewUser'))
        sm.add_widget(Dashboard(name='Dashboard'))
        sm.add_widget(Search(name='Search'))
        sm.add_widget(Profil(name='Profil'))
        sm.add_widget(Construction(name='Construction'))
        sm.add_widget(Recipe(name='Recipe'))
        sm.add_widget(RecipeOfTheDayScreen(name='RecipeOfTheDay'))

        # Setze den ScreenManager als Root-Widget der App
        self.root = sm
        return self.root