class TaskManager:
    def __init__(self):
        self.aufgaben = []

    def aufgabe_hinzufuegen(self, name, start, dauer):
        if not name or not start or not dauer:
            return False, "Bitte alle Felder ausfüllen."
        
        try:
            dauer_int = int(dauer)
        except ValueError:
            return False, "Dauer muss eine Zahl sein."
        
        self.aufgaben.append((name, start, dauer))
        return True, "Aufgabe wurde hinzugefügt!"
    
    def get_aufgaben(self):
        return self.aufgaben
    
    def aufgabe_loeschen(self, index):
        if 0 <= index < len(self.aufgaben):
            del self.aufgaben[index]
            return True
        return False
    