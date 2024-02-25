# Hauptanwendungsskript

# Module, die man installieren muss, damit Kivy funktioniert
# python -m pip install kivy[base] kivy_examples
# python -m pip install pygame
# pip install https://github.com/kivymd/KivyMD/archive/master.zip für KiviMD 2.0.1

from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDockedDatePicker
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivy.properties import StringProperty

class CommonNavigationRailItem(MDNavigationRailItem):
   text = StringProperty()
   icon = StringProperty()

#Definieren der verschiedenen Screens:
class Welcome(MDScreen):
   pass

class CreateUser(MDScreen):
   pass
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

# Loading multible .kv Design files
      Builder.load_file("pages/welcome.kv", encoding="utf8")
      Builder.load_file("pages/registration.kv", encoding="utf8")
      Builder.load_file("pages/dashboard.kv", encoding="utf8")
      Builder.load_file("pages/search.kv", encoding="utf8")
      '''Builder.load_file("pages/login.kv", encoding="utf8")'''

# Definition verschiedner Layouts (Aktuell nur "Darkmode")
      self.theme_cls.theme_style = "Dark"
      self.theme_cls.primary_palette = "Darkgreen" 

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

