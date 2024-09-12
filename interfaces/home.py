import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem
)

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz de Inventario")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        
        # Formulario para agregar artículos
        self.form_layout = QHBoxLayout()
        
        self.name_label = QLabel("Nombre del Artículo:")
        self.name_input = QLineEdit()
        
        self.quantity_label = QLabel("Cantidad:")
        self.quantity_input = QLineEdit()
        
        self.add_button = QPushButton("Agregar")
        self.add_button.clicked.connect(self.add_item)
        
        self.form_layout.addWidget(self.name_label)
        self.form_layout.addWidget(self.name_input)
        self.form_layout.addWidget(self.quantity_label)
        self.form_layout.addWidget(self.quantity_input)
        self.form_layout.addWidget(self.add_button)
        
        self.layout.addLayout(self.form_layout)
        
        # Tabla para mostrar el inventario
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Artículo", "Cantidad"])
        self.layout.addWidget(self.table)
        
        self.setLayout(self.layout)

    def add_item(self):
        name = self.name_input.text()
        quantity = self.quantity_input.text()
        
        if name and quantity:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(quantity))
            
            self.name_input.clear()
            self.quantity_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec())