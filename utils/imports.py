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
from utils.search import search_combined
from kivy.core.window import Window
from kivy.modules import inspector
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
