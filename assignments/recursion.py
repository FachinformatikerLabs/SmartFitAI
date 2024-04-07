import time

def countdown(n):
    if n <= 0:
        return
    print (f"Geht zurück auf die Suchseite in {n} sekunden")
    time.sleep(1)
    return countdown(n = n - 1)