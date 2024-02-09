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

Window.size = (800,800)
#Definieren der verschiedenen Screens:
class FirstWindow(Screen):

    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("resources\SmartFit_GUI.kv", encoding="utf8")

class SmartFitAIApp(App):
    def build(self):
        Window.clearcolor = (85/255, 110/255, 83/255, 1)
        return kv
    
    
if __name__=="__main__":
    SmartFitAIApp().run()

