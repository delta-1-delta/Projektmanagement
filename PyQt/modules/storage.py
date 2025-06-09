import json

def speichere_aufgaben(dateipfad, aufgabenliste):
    with open(dateipfad, "w", encoding="utf-8") as f:
        json.dump(aufgabenliste, f)

def lade_aufgaben(dateipfad):
    try:
        with open(dateipfad,"r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []