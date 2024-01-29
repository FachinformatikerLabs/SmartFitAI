# Hauptanwendungsskript

# Spielereien mit kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window


class MyApp(App):
    def build(self):
        Window.clearcolor = (0.4, 0.9, 0.2, 0.85)
        layout = FloatLayout()
        label1 = Label(text = "SmartFitAI", size_hint=(0.5, 0.5), pos_hint={"center_x":0.5, "center_y":0.8}, font_size="30sp")
        label2 = Label(text = "Gesund und bewusst essen \nund dabei nicht die Nährwerte aus dem Auge verlieren", size_hint=(0.5, 0.7), pos_hint={"center_x":0.5, "center_y":0.5})
        button1 = Button(text = "New User", size_hint=(0.2, 0.1), pos_hint={"center_x": 0.25, "center_y" : 0.3})
        button2 = Button(text = "Login", size_hint=(0.2, 0.1), pos_hint={"center_x": 0.75, "center_y" : 0.3})
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(button1)
        layout.add_widget(button2)

      
        return layout
    
if __name__ == "__main__":
    MyApp().run()
