from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel)

class GraphInfoWidget(QWidget):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Vertex count
        self.vertex_count_label = QLabel()
        layout.addWidget(self.vertex_count_label)

        # Edge count
        self.edge_count_label = QLabel()
        layout.addWidget(self.edge_count_label)

        # Component count
        self.components_count_label = QLabel()
        layout.addWidget(self.components_count_label)

        # Bipartite check
        self.bipartite_label = QLabel()
        layout.addWidget(self.bipartite_label)

        self.update_info()
        self.setLayout(layout)

    def update_info(self):
        self.vertex_count_label.setText(f"Num Vertices: {self.graph.getNumVertices()}")
        self.edge_count_label.setText(f"Num Edges: {self.graph.getNumEdges()}")
        self.components_count_label.setText(f"Num Components: {self.graph.getNumComponents()}")
        self.bipartite_label.setText(f"Is Bipartite: {self.graph.getIsBipartite()}")
