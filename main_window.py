from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter
from PyQt6.QtCore import Qt
from graph_widget import GraphWidget
from add_feature_widget import FeatureWidget

class GraphTheorySketchpad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.graphWidget = GraphWidget()
        self.graph = self.graphWidget.graph

        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        # Splitter for top (60%) and bottom (40%)
        self.vertical_splitter = QSplitter(Qt.Orientation.Vertical)
        self.main_layout.addWidget(self.vertical_splitter)

        # Top area widget and layout
        self.top_widget = QWidget()
        self.top_layout = QVBoxLayout(self.top_widget)
        self.top_layout.setContentsMargins(0, 0, 0, 0)

        # Splitter for left (50%) and right (50%) in the top area
        self.horizontal_splitter = QSplitter(Qt.Orientation.Horizontal)
        self.top_layout.addWidget(self.horizontal_splitter)
        self.top_widget.setLayout(self.top_layout)

        # Splitter for dividing the left panel into top and bottom
        self.left_vertical_splitter = QSplitter(Qt.Orientation.Vertical)
        self.left_panel_upper = FeatureWidget(self.graph)
        # self.left_panel_upper.setStyleSheet("background-color: navy;") 
        self.left_panel_lower = QWidget()
        self.left_panel_lower.setStyleSheet("background-color: lightcoral;")

        # Add widgets to the vertical splitter in the left panel
        self.left_vertical_splitter.addWidget(self.left_panel_upper)
        self.left_vertical_splitter.addWidget(self.left_panel_lower)

        # Add the left vertical splitter to the horizontal splitter
        self.horizontal_splitter.addWidget(self.left_vertical_splitter)

        # Graph Panel
        self.right_panel = self.graphWidget
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
        self.left_vertical_splitter.setSizes([int(self.left_vertical_splitter.height() * 0.6), int(self.left_vertical_splitter.height() * 0.4)])

        # Set the window title
        self.setWindowTitle("Graph Theory Sketchpad")

        # Set minimum size
        self.setMinimumSize(800, 600)

        # Show the main window
        self.show()
