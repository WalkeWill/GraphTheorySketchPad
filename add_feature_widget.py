from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox)

class FeatureWidget(QWidget):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel('Add Element')
        layout.addWidget(title)

        # Add Vertice Section
        layout.addWidget(QLabel('Add Vertice'))
        self.vertice_label_input = QLineEdit()
        self.vertice_label_input.setPlaceholderText('Enter vertice label')
        layout.addWidget(self.vertice_label_input)

        self.color_dropdown = QComboBox()
        self.color_dropdown.addItems(['Black', 'Green', 'Blue', 'Yellow', 'Purple'])
        layout.addWidget(self.color_dropdown)

        add_vertice_button = QPushButton('Add')
        add_vertice_button.clicked.connect(self.add_vertice)
        layout.addWidget(add_vertice_button)

        # Add Edge Section
        layout.addWidget(QLabel('Add Edge'))
        edge_hbox = QHBoxLayout()

        self.start_vertice_input = QLineEdit()
        self.start_vertice_input.setPlaceholderText('Start vertice')
        edge_hbox.addWidget(self.start_vertice_input)

        self.end_vertice_input = QLineEdit()
        self.end_vertice_input.setPlaceholderText('End vertice')
        edge_hbox.addWidget(self.end_vertice_input)

        layout.addLayout(edge_hbox)

        add_edge_button = QPushButton('Add')
        add_edge_button.clicked.connect(self.add_edge)
        layout.addWidget(add_edge_button)

        self.setLayout(layout)

    def add_vertice(self):
        label = self.vertice_label_input.text()
        color = self.color_dropdown.currentText()
        if label in self.graph.verticeLabels:
            # Popup window saying they cant have multiple vertices with same name
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Duplicate vertex label!")
            msg.setInformativeText("Each vertex must have a unique label.")
            msg.setWindowTitle("Error")
            msg.exec()
            return

        self.graph.add_vertex(label, color)

    def add_edge(self):
        start = self.start_vertice_input.text()
        end = self.end_vertice_input.text()
        if start not in self.graph.verticeLabels or end not in self.graph.verticeLabels:
            # Popup window saying the vertices doesnt exist
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("One of the entered vertices does not exist!")
            msg.setInformativeText("Please add more vertices or change the entered vertices.")
            msg.setWindowTitle("Error")
            msg.exec()
            return

        self.graph.add_edge(start, end)