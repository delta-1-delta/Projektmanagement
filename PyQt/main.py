import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton,
QListWidget)
class GanttFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gantt-3000")
        self.setGeometry(100, 100, 500, 400)

        #Aufgabenliste
        self.aufgaben =[]

        #Oberfläche
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #Layout
        layout = QVBoxLayout()
        
        #Eingabefelder
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Name der Aufgabe")
        
        self.input_start = QLineEdit()
        self.input_start.setPlaceholderText("Das Startdatum(z.B. 2025-06-09)")

        self.input_dauer = QLineEdit()
        self.input_dauer.setPlaceholderText("Dauer(in Tagen)")

        #Button
        self.button_hinzufuegen = QPushButton("Hinzufügen")
        self.button_hinzufuegen.clicked.connect(self.aufgabe_hinzufuegen)

        #Platzhalter für spätere Ausgabe
        self.ausgabe_label = QLabel("Noch keine Aufgaben hinzugefügt")

        #Aufgabenliste konvertiert in Widget
        self.liste_widget = QListWidget()

        #Elemente ins Layout
        layout.addWidget(self.input_name)
        layout.addWidget(self.input_start)
        layout.addWidget(self.input_dauer)
        layout.addWidget(self.button_hinzufuegen)
        layout.addWidget(self.ausgabe_label)
        layout.addWidget(self.liste_widget)

        central_widget.setLayout(layout) 

    def aufgabe_hinzufuegen(self):
        name = self.input_name.text()
        start = self.input_start.text()
        dauer = self.input_dauer.text()
    
        if name and start and dauer:
            eintrag = F"{name} | Start: {start} | Dauer: {dauer} Tage"
            

        self.ausgabe_label.setText(f"Aufgabe: {name}, Start: {start}, Dauer: {dauer} Tage")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GanttFenster()  
    window.show()
    sys.exit(app.exec_()) 

    


