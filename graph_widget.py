from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt, QRectF
from graph import Graph

class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.graph = Graph()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.view = QGraphicsView(self.graph)
        self.view.setRenderHints(QPainter.RenderHint.Antialiasing)
        layout.addWidget(self.view)

        # Horizontal layout for zoom controls
        self.zoom_layout = QHBoxLayout()
        self.zoom_in_button = QPushButton("+")
        self.zoom_out_button = QPushButton("-")
        self.zoom_layout.addWidget(self.zoom_in_button)
        self.zoom_layout.addWidget(self.zoom_out_button)
        self.zoom_layout.addStretch()  # Pushes the buttons to the right
        layout.addLayout(self.zoom_layout)

        # Connect buttons to their functions
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_out_button.clicked.connect(self.zoom_out)

        # Disable scrollbars
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scale_factor = 1.1  # Scale factor for zoom

    def adjust_size(self):
        self.graph.setSceneRect(QRectF(self.view.viewport().rect()))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_size()

    def zoom_in(self):
        self.view.scale(self.scale_factor, self.scale_factor)

    def zoom_out(self):
        self.view.scale(1 / self.scale_factor, 1 / self.scale_factor)
