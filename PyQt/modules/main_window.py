from PyQt5.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, 
QPushButton ,QListWidget)
from modules.gantt_plot import plot_gantt, exportiere_gantt_pdf
from modules.task_manager import TaskManager
from modules.storage import speichere_aufgaben, lade_aufgaben
import os

class GanttFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gantt-3000")
        self.setGeometry(100, 100, 1000, 700)
        self.canvas = None
        self.taskmanager = TaskManager()
        projektpfad = os.path.dirname(os.path.abspath(__file__))
        datenordner = os.path.join(projektpfad, "..", "daten")
        os.makedirs(datenordner, exist_ok=True)
        self.dateipfad = os.path.join(datenordner, "aufgaben.json")

        
        #Oberfläche
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #Layout
        self.layout = QVBoxLayout()
        
        #Eingabefelder
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Name der Aufgabe")
        
        self.input_start = QLineEdit()
        self.input_start.setPlaceholderText("Das Startdatum(Format YYYY-MM-DD z.B.: 2025-06-09)")

        self.input_dauer = QLineEdit()
        self.input_dauer.setPlaceholderText("Dauer(in Tagen)")

        #Button
        self.button_hinzufuegen = QPushButton("Hinzufügen")
        self.button_hinzufuegen.clicked.connect(self.aufgabe_hinzufuegen)

        self.button_anzeigen = QPushButton("Diagramm anzeigen")
        self.button_anzeigen.clicked.connect(self.gantt_anzeigen)
        
        self.button_loeschen = QPushButton("Ausgewählte Aufgabe löschen")
        self.button_loeschen.clicked.connect(self.aufgabe_loeschen)
        self.layout.addWidget(self.button_loeschen)

        self.button_exportieren = QPushButton("Diagramm als PDF speichern")
        self.button_exportieren.clicked.connect(self.gantt_exportieren)
        self.layout.addWidget(self.button_exportieren)

        #Platzhalter für spätere Ausgabe
        self.ausgabe_label = QLabel("Noch keine Aufgaben hinzugefügt")

        #Aufgabenliste konvertiert in Widget
        self.liste_widget = QListWidget()

        #laden und anzeigen von gespeicherten Aufgaben
        gespeicherte_aufgaben = lade_aufgaben(self.dateipfad)
        for name, start, dauer in gespeicherte_aufgaben:
            erfolg, _ =self.taskmanager.aufgabe_hinzufuegen(name, start, dauer)
            if erfolg:
                eintrag = f"{name} | Start: {start} | Dauer: {dauer} Tage"
                self.liste_widget.addItem(eintrag)

        #Elemente ins Layout
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.input_start)
        self.layout.addWidget(self.input_dauer)
        self.layout.addWidget(self.button_hinzufuegen)
        self.layout.addWidget(self.ausgabe_label)
        self.layout.addWidget(self.liste_widget)
        self.layout.addWidget(self.button_anzeigen)

        central_widget.setLayout(self.layout) 

    def aufgabe_hinzufuegen(self):
        name = self.input_name.text()
        start = self.input_start.text()
        dauer = self.input_dauer.text()

        erfolg, meldung = self.taskmanager.aufgabe_hinzufuegen(name, start, dauer)
        self.ausgabe_label.setText(meldung)

        if erfolg:
            eintrag = f"{name} | Start: {start} | Dauer: {dauer} Tage" 
            self.liste_widget.addItem(eintrag)
            self.input_name.clear()
            self.input_start.clear()
            self.input_dauer.clear()
            
            speichere_aufgaben(self.dateipfad, self.taskmanager.get_aufgaben())
        else:
            self.ausgabe_label.setText("Füllen Sie bitte alle Felder aus!")
            

    def gantt_anzeigen(self):
        aufgaben = self.taskmanager.get_aufgaben()

        if not aufgaben:
            self.ausgabe_label.setText("Keine Aufgaben vorhanden.")
            return
        #enfernt altes Gantt Diagramm wenn vorhanden
        if hasattr(self, "canvas") and self.canvas is not None:
            self.layout.removeWidget(self.canvas)
            self.canvas.setParent(None)
            self.canvas.deleteLater()
            self.canvas = None

        
        self.canvas = plot_gantt(aufgaben)
        self.layout.addWidget(self.canvas)

    def aufgabe_loeschen(self):
        index = self.liste_widget.currentRow()
        if index < 0:
            self.ausgabe_label.setText("Bitte zuerst eine Aufgabe auswählen.")
            return

        erfolg = self.taskmanager.aufgabe_loeschen(index)
        if erfolg:
            self.liste_widget.takeItem(index)
            self.ausgabe_label.setText("Aufgabe gelöscht.")
            speichere_aufgaben(self.dateipfad, self.taskmanager.get_aufgaben())

            # ggf. Gantt-Diagramm aktualisieren
            if hasattr(self, "canvas") and self.canvas is not None:
                self.gantt_anzeigen()
        else:
            self.ausgabe_label.setText("Löschen fehlgeschlagen.")
    def gantt_exportieren(self):
        aufgaben = self.taskmanager.get_aufgaben()
        if not aufgaben:
            self.ausgabe_label.setText("Keine Aufgaben vorhanden.")
            return

        projektpfad = os.path.dirname(os.path.abspath(__file__))
        datenordner = os.path.join(projektpfad, "..", "daten")
        os.makedirs(datenordner, exist_ok=True)
        pfad = os.path.join(datenordner, "gantt_export.pdf")
        from modules.gantt_plot import exportiere_gantt_pdf
        erfolg, meldung = exportiere_gantt_pdf(aufgaben, pfad)
        self.ausgabe_label.setText(meldung)
    