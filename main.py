import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QPainter
from graph import Graph

class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = QGraphicsView()
        self.graph = Graph()
        self.view.setScene(self.graph)
        self.setCentralWidget(self.view)
        self.setMinimumSize(600, 400)
        self.setWindowTitle("Graph Sketchpad")
        self.view.setRenderHints(QPainter.RenderHint.Antialiasing)
        self.graph.setSceneRect(QRectF(self.view.viewport().rect()))
        self.show()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.graph.setSceneRect(QRectF(self.view.viewport().rect()))
        self.graph.update_graphics()

def main():
    app = QApplication(sys.argv)
    mainWindow = GraphWindow()
    graph = mainWindow.graph
    graph.add_vertex('v1')
    graph.add_vertex('v2')
    graph.add_vertex('v3')
    graph.add_vertex('v4')
    graph.add_edge(graph.vertices[0],graph.vertices[1])
    graph.add_edge(graph.vertices[2],graph.vertices[3])
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
