import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplitter
from PyQt6.QtCore import Qt
from graph_window import GraphWidget
    
class GraphTheorySketchpad(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        # Splitter for top (60%) and bottom (40%)
        self.vertical_splitter = QSplitter(Qt.Orientation.Vertical)
        self.main_layout.addWidget(self.vertical_splitter)

        # Top area widget and layout (will hold another splitter)
        self.top_widget = QWidget()
        self.top_layout = QVBoxLayout(self.top_widget)
        self.top_layout.setContentsMargins(0, 0, 0, 0)  # Ensure no margins in the top layout

        # Splitter for left (50%) and right (50%) in the top area
        self.horizontal_splitter = QSplitter(Qt.Orientation.Horizontal)
        self.top_layout.addWidget(self.horizontal_splitter)
        self.top_widget.setLayout(self.top_layout)  # Set layout for top_widget

        # Placeholder widgets for the left and right panels in the top area
        self.left_panel = QWidget()
        self.left_panel.setStyleSheet("background-color: lightblue;")
        self.horizontal_splitter.addWidget(self.left_panel)

        self.right_panel = GraphWidget()
        self.right_panel.setStyleSheet("background-color: darkgrey;")
        self.horizontal_splitter.addWidget(self.right_panel)

        # Placeholder widget for the bottom area
        self.bottom_panel = QWidget()
        self.bottom_panel.setStyleSheet("background-color: lightgrey;")
        self.vertical_splitter.addWidget(self.top_widget)
        self.vertical_splitter.addWidget(self.bottom_panel)

        # Set initial sizes for splitters to maintain the proportions
        self.vertical_splitter.setSizes([int(self.height() * 0.6), int(self.height() * 0.4)])
        self.horizontal_splitter.setSizes([int(self.width() * 0.4), int(self.width() * 0.6)])

        # Set the window title
        self.setWindowTitle("Graph Theory Sketchpad")

        # Set minimum size or default size
        self.setMinimumSize(800, 600)  # Set the minimum size of the window

        # Show the main window
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = GraphTheorySketchpad()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()