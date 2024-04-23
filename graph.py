from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QBrush, QColor
from edge import Edge
from vertex import VertexNode

class Graph(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(0, 0, 600, 400)  # Scene size
        self.setBackgroundBrush(QBrush(QColor(240, 240, 240)))
        self.vertices = []
        self.edges = []

    def add_vertex(self, label, diameter=30):
        x = 100 + len(self.vertices) * 100
        y = 100 + len(self.vertices) * 100
        vertex = VertexNode(label, diameter)
        vertex.setPos(x, y)
        self.addItem(vertex)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, vertex1, vertex2):
        edge = Edge(vertex1, vertex2)
        self.addItem(edge)
        self.edges.append(edge)
        self.update_graphics()
        return edge

    def update_graphics(self):
        for edge in self.edges:
            edge.update_position()
