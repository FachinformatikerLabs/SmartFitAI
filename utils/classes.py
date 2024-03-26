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
         
class SearchResultCard(MDCard):
    def __init__(self, recipe_name, image_url, **kwargs):
        super().__init__(**kwargs)
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

class SearchBar(BoxLayout):
    def on_search(self, query):
        app = MDApp.get_running_app()
        results = search_combined(query)
        
        if results:
            app.root.current = 'Search'
            search_screen = app.root.get_screen('Search')
            search_screen.display_results(results)
        
class Search(MDScreen):
    def display_results(self, results):
        self.ids.results_grid.clear_widgets()
        for result in results:
            # Erstelle eine neue SearchResultCard
            card = SearchResultCard(recipe_name=result['recipe_name'], image_url=result['image_url'])
            # Füge die neue Karte dem GridLayout hinzu
            self.ids.results_grid.add_widget(card)

class Construction(MDScreen):
    pass

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

    def build(self):
        self.supabase = supabase
        inspector.create_inspector(Window, self)

        # Laden der verschiedenen .kv Design Files 
        Builder.load_file("pages/login.kv", encoding="utf8")
        Builder.load_file("pages/registration.kv", encoding="utf8")
        Builder.load_file("pages/dashboard.kv", encoding="utf8")
        Builder.load_file("pages/search.kv", encoding="utf8")
        Builder.load_file("pages/profil.kv", encoding="utf8")
        Builder.load_file("pages/construction.kv", encoding="utf8")
        Builder.load_file("components/nav.kv", encoding="utf8")
        Builder.load_file("components/searchbar.kv", encoding="utf8")
        Builder.load_file("components/background.kv", encoding="utf8")
        
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

        # Setze den ScreenManager als Root-Widget der App
        self.root = sm
        return self.root
