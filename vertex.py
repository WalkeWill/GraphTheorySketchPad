from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem
from PyQt6.QtGui import QBrush, QColor, QFont

class VertexNode(QGraphicsEllipseItem):
    def __init__(self, label, color=QColor(0, 0, 255), diameter=30):
        super().__init__(0, 0, diameter, diameter)
        self.setBrush(QBrush(color))  # Blue Vertices
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable, True)
        self.diameter = diameter
        self.setZValue(1)
        self.name = label

        self.label = QGraphicsTextItem(label, self)
        self.label.setDefaultTextColor(QColor(255, 0, 0))  # Red Text
        font = QFont("Arial", 20) 
        self.label.setFont(font)

    # Move vertices with mouse
    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self.constrain_within_bounds()
        self.scene().update_graphics()

    # Dont let vertices move out of window.
    def constrain_within_bounds(self):
        new_pos = self.pos()
        scene_rect = self.scene().sceneRect()
        x = max(scene_rect.left(), min(new_pos.x(), scene_rect.right() - self.diameter))
        y = max(scene_rect.top(), min(new_pos.y(), scene_rect.bottom() - self.diameter))
        self.setPos(x, y)