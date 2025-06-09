import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class GanttFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gantt-3000")
        self.setGeometry(100, 100, 500, 400)

        self.button = QPushButton("Gantt anzeigen")
        self.button.clicked.connect(self.show_gantt)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def show_gantt(self):
        print

