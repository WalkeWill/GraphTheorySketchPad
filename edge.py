from PyQt6.QtWidgets import QGraphicsLineItem
from PyQt6.QtCore import QPointF, QLineF
from PyQt6.QtGui import QPen, QColor

class Edge(QGraphicsLineItem):
    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end
        self.update_position()
        self.setPen(QPen(QColor(255, 255, 255), 2))

    def update_position(self):
        self.setLine(QLineF(self.start.pos() + QPointF(15, 15), self.end.pos() + QPointF(15, 15)))
        self.setPen(QPen(QColor(0, 0, 0), 2))  # Black color for the edge