# Hauptanwendungsskript

# Module, die man installieren muss, damit Kivy funktioniert
# python -m pip install kivy[base] kivy_examples
# python -m pip install pygame

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

#Definieren der verschiedenen Screens:
class Welcome(Screen):
   pass

class CreateUser(Screen):
   pass

class Dashboard(Screen):
   pass

class RecipeSearch(Screen):
   pass

class IngredientSearch(Screen):
   pass

class AllergenSearch(Screen):
   pass

class WindowManager(ScreenManager):
   pass

# Loading multible .kv Design files
Builder.load_file("pages/welcome.kv", encoding="utf8")
Builder.load_file("pages/registration.kv", encoding="utf8")
Builder.load_file("pages/dashboard.kv", encoding="utf8")
Builder.load_file("pages/search.kv", encoding="utf8")
'''Builder.load_file("pages/login.kv", encoding="utf8")'''

class SmartFitAIApp(App):
   def build(self):
      Window.size = (800,800)                                  # Window Size for all Views
      Window.clearcolor = (85/255, 110/255, 83/255, 1)         # Window Color for all Views
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

