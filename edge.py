from PyQt6.QtWidgets import QGraphicsLineItem, QGraphicsEllipseItem
from PyQt6.QtCore import QPointF, QLineF
from PyQt6.QtGui import QPen, QColor

class StraightEdge(QGraphicsLineItem):
    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end
        self.update_position()
        self.setPen(QPen(QColor(255, 255, 255), 2))

    def update_position(self):
        self.setLine(QLineF(self.start.pos() + QPointF(15, 15), self.end.pos() + QPointF(15, 15)))
        self.setPen(QPen(QColor(0, 0, 0), 2))  # Black color for the edge

class Loop(QGraphicsEllipseItem):
    def __init__(self, vertex, diameter=30, loop_diameter=40):
        super().__init__()
        self.vertex = vertex
        self.diameter = diameter
        self.loop_diameter=loop_diameter
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.setBrush(QColor(0, 0, 0, 0))
        self.update_position()

    def update_position(self):
        # Calculate the offset to center the loop around the vertex
        x = self.vertex.pos().x() + self.diameter / 2 - self.loop_diameter / 2
        y = self.vertex.pos().y() - self.loop_diameter / 2
        self.setRect(x, y, self.loop_diameter, self.loop_diameter)

class CurvedEdge(QGraphicsLineItem):
    # For parallel edges
    pass
