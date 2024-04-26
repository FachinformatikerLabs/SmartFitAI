# TODO: Rekursion: Ein Countdown Timer der rekursiv funktioniert dieser wird aufgerufen wenn der Zurück-Button angeklickt wird
import time
#zählt von n runter auf 1
def countdown(n):
    if n <= 0:
        return
    print (f"Geht zurück auf die Suchseite in {n} sekunden")
    time.sleep(1)
    return countdown(n = n - 1)