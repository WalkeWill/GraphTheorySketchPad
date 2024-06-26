from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QBrush, QColor
from edge import Loop, Edge
from vertex import VertexNode
from collections import defaultdict
import copy

class Graph(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackgroundBrush(QBrush(QColor(240, 240, 240)))
        self.vertices = []
        self.verticeLabels = {}
        self.edges = []
        self.edgeLabels = defaultdict(int)

    def add_vertex(self, label, color='Blue', diameter=30):
        diameter = 30
        x = 100 + (len(self.vertices) % 5) * 50 
        y = 100 + int(len(self.vertices) / 5) * 50
        vertex = VertexNode(label, color, diameter)
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
    
    def delete_edge(self, edge):
        self.removeItem(edge)
        self.edges.remove(edge)
        self.edgeLabels[(edge.start.name, edge.end.name)] -= 1
        self.update_graphics

    def delete_vertex(self, vertex):
        self.removeItem(vertex)
        self.vertices.remove(vertex)
        del self.verticeLabels[vertex.name]
        # Need to delete all edges connected to this vertex as well.
        for edge in list(self.edges):
            if edge.start == vertex or edge.end == vertex:
                self.removeItem(edge)
                self.edges.remove(edge)
                self.edgeLabels[(edge.start.name, edge.end.name)] -= 1
        self.update_graphics

    def update_graphics(self):
        for edge in self.edges:
            edge.update_position()

    def getNumVertices(self):
        return len(self.vertices)
    
    def getNumEdges(self):
        return len(self.edges)
    
    def get_degree(self, vertex):
        degree = 0
        for e in self.edgeLabels:
            if vertex.name in e:
                if e[0] == e[1]:
                    # Double degree count for loops
                    degree += 2 * self.edgeLabels[e]
                else:
                    degree += self.edgeLabels[e]
        return degree
    
    def getNumComponents(self):
        seen = []
        frontier = list(self.verticeLabels.keys())

        def dfs(node):
            if node not in seen:
                seen.append(node)
                edges = list(filter(lambda x: self.edgeLabels[x] > 0 and node in x, self.edgeLabels))
                for v1, v2 in edges:
                    seen.append(v1)
                    dfs(v1)
                    dfs(v2)

        total_components = 0
        for vertex in frontier:
            if vertex not in seen:
                dfs(vertex)
                total_components += 1

        return total_components

    def getIsBipartite(self):
        colors = {}
        frontier = list(self.verticeLabels.keys())

        def dfs(node, color):
            if node in colors:
                return colors[node] == color
            colors[node] = color
            edges = list(filter(lambda x: self.edgeLabels[x] > 0 and node in x, self.edgeLabels))
            for neighbor in edges:
                if not dfs(neighbor[0], 1 - color) and not dfs(neighbor[1], 1 - color):
                    return False
            return True

        for vertex in frontier:
            if vertex not in colors:  # If vertex is not colored, it means it hasn't been visited
                if not dfs(vertex, 0):  # Start coloring with 0, alternates will be 1
                    return False
        return True
       
    
    def copy(self):
        new_graph = Graph()
        new_graph.vertices = list(self.vertices)
        new_graph.verticeLabels = dict(self.verticeLabels)
        new_graph.edgeLabels = dict(self.edgeLabels)
        new_graph.edges = list(self.edges)
        return new_graph

    def is_bridge(self, edge):
        new = self.copy()
        before = new.getNumComponents()
        new.edges.remove(edge)
        new.edgeLabels[(edge.start.name, edge.end.name)] -= 1
        after = new.getNumComponents()
        return before != after
