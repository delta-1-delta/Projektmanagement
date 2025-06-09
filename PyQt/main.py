import sys
from PyQt5.QtWidgets import QApplication
from modules.main_window import GanttFenster
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GanttFenster()  
    window.show()
    sys.exit(app.exec_()) 

    


