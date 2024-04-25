from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter
from PyQt6.QtCore import Qt
from widgets.graph_widget import GraphWidget
from widgets.add_feature_widget import FeatureWidget
from widgets.graph_info_widget import GraphInfoWidget
from widgets.vertex_widget import VertexWidget
from widgets.edge_widget import EdgeWidget

class GraphTheorySketchpad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.graphWidget = GraphWidget()
        self.graph = self.graphWidget.graph
        self.info = GraphInfoWidget(self.graph)
        self.deleteEdge = EdgeWidget(self.graph,self.info)
        self.deleteVertex = VertexWidget(self.graph,self.info, self.deleteEdge)
        self.addFeature = FeatureWidget(self.graph, self.info, self.deleteVertex, self.deleteEdge)

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
        self.left_panel_upper = self.addFeature
        self.left_panel_lower = self.info

        # Add widgets to the vertical splitter in the left panel
        self.left_vertical_splitter.addWidget(self.left_panel_upper)
        self.left_vertical_splitter.addWidget(self.left_panel_lower)

        # Add the left vertical splitter to the horizontal splitter
        self.horizontal_splitter.addWidget(self.left_vertical_splitter)

        # Graph Panel
        self.right_panel = self.graphWidget
        self.horizontal_splitter.addWidget(self.right_panel)

        # Bottom area setup with a horizontal splitter for 50% left and 50% right
        self.bottom_horizontal_splitter = QSplitter(Qt.Orientation.Horizontal)
        self.vertical_splitter.addWidget(self.top_widget)
        self.vertical_splitter.addWidget(self.bottom_horizontal_splitter)

        # Left panel in the bottom area for DeleteFeatureWidget
        self.bottom_left_panel = self.deleteVertex
        self.bottom_horizontal_splitter.addWidget(self.bottom_left_panel)

        # Right panel in the bottom area
        self.bottom_right_panel = self.deleteEdge
        self.bottom_horizontal_splitter.addWidget(self.bottom_right_panel)

        # Set initial sizes for splitters to maintain the proportions
        self.vertical_splitter.setSizes([int(self.height() * 0.45), int(self.height() * 0.55)])
        self.horizontal_splitter.setSizes([int(self.width() * 0.4), int(self.width() * 0.6)])
        self.left_vertical_splitter.setSizes([int(self.left_vertical_splitter.height() * 0.6), int(self.left_vertical_splitter.height() * 0.4)])
        self.bottom_horizontal_splitter.setSizes([int(self.width() * 0.5), int(self.width() * 0.5)])

        # Set the window title and size
        self.setWindowTitle("Graph Theory Sketchpad")
        self.setMinimumSize(800, 600)
        self.show()
