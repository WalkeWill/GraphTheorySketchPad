from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import QRectF
from edge import Loop, Edge
from vertex import VertexNode
from collections import defaultdict

class Graph(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackgroundBrush(QBrush(QColor(240, 240, 240)))
        self.vertices = []
        self.verticeLabels = {}
        self.edges = []
        self.edgeLabels = defaultdict(int)
        self.add_vertex('v1')
        self.add_vertex('v2')
        self.add_vertex('v3')
        self.add_edge('v1', 'v2')
        self.add_edge('v1', 'v1')
        self.add_edge('v2', 'v1')
        self.add_edge('v1', 'v2')

    def add_vertex(self, label, diameter=30):
        x = 100 + (len(self.vertices) % 5) * 50 
        y = 100 + int(len(self.vertices) / 5) * 50
        vertex = VertexNode(label, diameter)
        vertex.setPos(x, y)
        self.addItem(vertex)
        self.vertices.append(vertex)
        self.verticeLabels[label] = vertex
        return vertex

    def add_edge(self, vertex1, vertex2):
        # Check if loop, parallel edge, or normal edge 
        if vertex1 == vertex2:
            edge = Loop(self.verticeLabels[vertex1])
        else:
            total = self.edgeLabels[(vertex1,vertex2)] + self.edgeLabels[(vertex2,vertex1)]
            edge = Edge(self.verticeLabels[vertex1], self.verticeLabels[vertex2], total * 30)
        
        self.addItem(edge)
        self.edges.append(edge)
        self.edgeLabels[(vertex1, vertex2)] += 1
        self.update_graphics()
        return edge

    def update_graphics(self):
        for edge in self.edges:
            edge.update_position()

    def update_scene_bounds(self):
        # Adjust scene bounds to the current view size
        view_rect = self.views()[0].viewport().rect()
        self.setSceneRect(QRectF(view_rect))
