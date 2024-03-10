# Hauptanwendungsskript

# Module, die man installieren muss, damit Kivy funktioniert
# python -m pip install kivy[base] kivy_examples
# python -m pip install pygame
# pip install https://github.com/kivymd/KivyMD/archive/master.zip für KiviMD 2.0.1
# ihr müsst jetzt auch bcrypt installieren bcrypt https://pypi.org/project/bcrypt/ da wir von der superbase signup auf eine eigene umgestiegen sind. in der wir einfach die datenbank füllen und unsere eigene login logik schreiben. Da passwörter nicht klar gespeichert werden nutzen wir bcrypt für die verschlüsselung des passworts


from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDockedDatePicker
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivy.properties import StringProperty
from database.conn import supabase
from datetime import datetime
import bcrypt


class CommonNavigationRailItem(MDNavigationRailItem):
   text = StringProperty()
   icon = StringProperty()

#Definieren der verschiedenen Screens:
class Welcome(MDScreen):
   pass

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

class Dashboard(MDScreen):
   pass

class RecipeSearch(MDScreen):
   pass

class IngredientSearch(MDScreen):
   pass

class AllergenSearch(MDScreen):
   pass

class WindowManager(ScreenManager):
   pass

class SmartFitAIApp(MDApp):
   def build(self):
      self.supabase = supabase


# Loading multible .kv Design files
      Builder.load_file("pages/welcome.kv", encoding="utf8")
      Builder.load_file("pages/registration.kv", encoding="utf8")
      Builder.load_file("pages/dashboard.kv", encoding="utf8")
      Builder.load_file("pages/search.kv", encoding="utf8")
      # Builder.load_file("pages/login.kv", encoding="utf8")

# Definition verschiedner Layouts (Aktuell nur "Darkmode")
      self.theme_cls.theme_style = "Dark"
      self.theme_cls.primary_palette = "Darkblue" 

      Window.size = (1920,1080)

      sm = WindowManager()
      sm.add_widget(Welcome(name='Welcome'))
      sm.add_widget(CreateUser(name='NewUser'))
      sm.add_widget(Dashboard(name='Dashboard'))
      sm.add_widget(RecipeSearch(name='RecipeSearch'))
      sm.add_widget(IngredientSearch(name='IngredientSearch'))
      sm.add_widget(AllergenSearch(name='AllergenSearch'))

      return sm

if __name__=="__main__":
   SmartFitAIApp().run()

