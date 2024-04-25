from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QSizePolicy

class EdgeWidget(QWidget):
    def __init__(self, graph, info):
        super().__init__()
        self.graph = graph
        self.info = info
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        
        # List for edges
        self.edge_list = QListWidget()
        self.layout.addWidget(self.edge_list)
        self.update_edge_list()

    def update_edge_list(self):
        self.edge_list.clear()
        for edge in self.graph.edges:
            widget = QWidget()
            layout = QHBoxLayout(widget)

            label = QLabel(f"{edge.start.name} -> {edge.end.name}")
            label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
            
            btn = QPushButton("Delete")
            btn.clicked.connect(lambda ch, e=edge: self.delete_edge(e))
            btn.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

            layout.addWidget(label)

            if self.graph.is_bridge(edge):
                bridge_label = QLabel('Bridge')
                bridge_label.setStyleSheet("color: red;")
                layout.addWidget(bridge_label)

            layout.addWidget(btn)

            item = QListWidgetItem(self.edge_list)
            item.setSizeHint(widget.sizeHint())
            self.edge_list.addItem(item)
            self.edge_list.setItemWidget(item, widget)

    def delete_edge(self, edge):
        self.graph.delete_edge(edge)
        self.update_edge_list()
        self.info.update_info()
