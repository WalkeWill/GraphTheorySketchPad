from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import QRectF
from edge import StraightEdge, Loop
from vertex import VertexNode

class Graph(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackgroundBrush(QBrush(QColor(240, 240, 240)))
        self.vertices = []
        self.labels = {}
        self.edges = []
        self.add_vertex('v1')
        self.add_vertex('v2')
        self.add_vertex('v3')
        self.add_edge('v1', 'v2')
        self.add_edge('v1', 'v1')

    def add_vertex(self, label, diameter=30):
        x = 100 + (len(self.vertices) % 5) * 50 
        y = 100 + int(len(self.vertices) / 5) * 50
        vertex = VertexNode(label, diameter)
        vertex.setPos(x, y)
        self.addItem(vertex)
        self.vertices.append(vertex)
        self.labels[label] = vertex
        return vertex

    def add_edge(self, vertex1, vertex2):
        # Check if loop, parallel edge, or normal edge 
        if vertex1 == vertex2:
            edge = Loop(self.labels[vertex1])
        else:
            edge = StraightEdge(self.labels[vertex1], self.labels[vertex2])
        
        self.addItem(edge)
        self.edges.append(edge)
        self.update_graphics()
        return edge

    def update_graphics(self):
        for edge in self.edges:
            edge.update_position()

    def update_scene_bounds(self):
        # Adjust scene bounds to the current view size
        view_rect = self.views()[0].viewport().rect()
        self.setSceneRect(QRectF(view_rect))
