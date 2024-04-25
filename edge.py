from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsPathItem
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPen, QColor, QPainterPath

class Loop(QGraphicsEllipseItem):
    def __init__(self, vertex, diameter=30, loop_diameter=40):
        super().__init__()
        self.start = vertex
        self.end = vertex
        self.diameter = diameter
        self.loop_diameter=loop_diameter
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.setBrush(QColor(0, 0, 0, 0))
        self.update_position()

    def update_position(self):
        # Calculate the offset to center the loop around the vertex
        x = self.start.pos().x() + self.diameter / 2 - self.loop_diameter / 2
        y = self.start.pos().y() - self.loop_diameter / 2
        self.setRect(x, y, self.loop_diameter, self.loop_diameter)

class Edge(QGraphicsPathItem):
    def __init__(self, start, end, curvature=50, color=QColor(0, 0, 0)):
        super().__init__()
        self.start = start
        self.end = end
        self.curvature = curvature
        self.setPen(QPen(color, 2))
        self.update_position()

    def update_position(self):
        if self.start and self.end:
            path = QPainterPath()
            start_point = self.start.pos() + QPointF(self.start.diameter / 2, self.start.diameter / 2)
            end_point = self.end.pos() + QPointF(self.end.diameter / 2, self.end.diameter / 2)

            control_point1 = QPointF(start_point.x(), start_point.y() + self.curvature)
            control_point2 = QPointF(end_point.x(), end_point.y() + self.curvature)

            path.moveTo(start_point)
            path.cubicTo(control_point1, control_point2, end_point)

            self.setPath(path)