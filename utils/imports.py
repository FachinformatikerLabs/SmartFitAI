from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDockedDatePicker
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from database.conn import supabase
from datetime import datetime
import bcrypt
import os
from dotenv import load_dotenv
from utils.search import get_recipe_details, get_ingredients_details, search_ingredient, search_recipe
from utils.nutritional_calculation import calculate_total_calories
from kivy.core.window import Window
from kivy.modules import inspector
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button