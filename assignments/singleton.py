#Dozentenaufgabe Singleton und Annotation
import datetime
from utils.search import get_random_recipe

class RecipeOfTheDay:
    #Klassenvariablen
    _last_update = None #Datum der letzten Aktualisierung speichern: am Anfang noch None
    _recipe_of_the_day = None #speichern des aufgerufenen Rezepts

# TODO: Singleton: statische Methode
    @staticmethod
    def get_recipe_of_the_day():
        today = datetime.date.today()
        if RecipeOfTheDay._last_update != today or RecipeOfTheDay._recipe_of_the_day is None:
            #Aktualisiere das Rezept, wenn es noch nicht gesetzt wurde oder ein neuer Tag begonnen hat
            RecipeOfTheDay._recipe_of_the_day = get_random_recipe()
            RecipeOfTheDay._last_update = today
            #Spezielle Nachricht je nach Tag
            message = RecipeOfTheDay.get_special_message(datetime.datetime.now())
            if RecipeOfTheDay._recipe_of_the_day:
                RecipeOfTheDay._recipe_of_the_day['special_message'] = message
        return RecipeOfTheDay._recipe_of_the_day


    @staticmethod
# TODO: Annotation: Typ-Hinweis Datum als String
    def get_special_message(date: datetime.datetime) -> str: 
        date_str = date.strftime('%m-%d') #Datum holen

        #Text zu bestimmten Tagen
        special_days = { 
            '01-01': "Frohes neues Jahr!",
            '02-02': "Tag des Murmeltiers",
            '02-14': "Happy Valentinstag!",
            '03-08': "Internationaler Frauentag",
            '03-17': "St. Patrick's Day!",
            '04-01': "April! April!",
            '04-22': "Tag der Erde",
            '04-30': "Walpurgisnacht!",
            '05-04': "May the Fourth be with you!",
            '05-05': "Cinco de Mayo",
            '06-05': "Weltumwelttag",
            '06-21': "Sommeranfang",
            '07-04': "Happy Independence Day!",
            '07-07': "Welt-Schokoladentag",
            '10-01': "Internationaler Kaffeetag",
            '10-31': "Happy Halloween!",
            '11-11': "Singles Day",
            '12-18': "Tag des Kinofilms",
            '12-25': "Frohe Weihnachten!",
            '12-31': "Silvester"
        }

        return special_days.get(date_str, "Genießen Sie das Rezept des Tages!")