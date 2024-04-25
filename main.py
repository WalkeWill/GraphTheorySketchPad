import sys
from PyQt6.QtWidgets import QApplication
from main_window import GraphTheorySketchpad
    
def main():
    app = QApplication(sys.argv)
    ex = GraphTheorySketchpad()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()