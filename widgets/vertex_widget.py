from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QSizePolicy

class VertexWidget(QWidget):
    def __init__(self, graph, info):
        super().__init__()
        self.graph = graph
        self.info = info
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        
        # List for vertices
        self.vertex_list = QListWidget()
        self.layout.addWidget(self.vertex_list)
        self.update_vertex_list()

    def update_vertex_list(self):
        self.vertex_list.clear()
        for vertex in self.graph.vertices:
            widget = QWidget()
            layout = QHBoxLayout(widget)
            
            label = QLabel(f"{vertex.name}")
            label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
            
            btn = QPushButton("Delete")
            btn.clicked.connect(lambda ch, v=vertex: self.delete_vertex(v))
            btn.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

            layout.addWidget(label)

            degree_label = QLabel(f"degree: {self.graph.get_degree(vertex)}")
            degree_label.setStyleSheet("color: red;")
            layout.addWidget(degree_label)

            layout.addWidget(btn)
            
            item = QListWidgetItem(self.vertex_list)
            item.setSizeHint(widget.sizeHint())
            self.vertex_list.addItem(item)
            self.vertex_list.setItemWidget(item, widget)

    def delete_vertex(self, vertex):
        self.graph.delete_vertex(vertex)
        self.update_vertex_list()
        self.info.update_info()
