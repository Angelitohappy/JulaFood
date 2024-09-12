import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem
)

class PersonRegistryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Personas")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        
        # Formulario para agregar personas
        self.form_layout = QVBoxLayout()
        
        self.first_name_label = QLabel("Primer Nombre:")
        self.first_name_input = QLineEdit()
        
        self.last_name_label = QLabel("Apellido:")
        self.last_name_input = QLineEdit()
        
        self.id_label = QLabel("Cédula:")
        self.id_input = QLineEdit()
        
        self.phone_label = QLabel("Teléfono:")
        self.phone_input = QLineEdit()
        
        self.address_label = QLabel("Dirección:")
        self.address_input = QLineEdit()
        
        self.add_button = QPushButton("Agregar")
        self.add_button.clicked.connect(self.add_person)
        
        self.form_layout.addWidget(self.first_name_label)
        self.form_layout.addWidget(self.first_name_input)
        self.form_layout.addWidget(self.last_name_label)
        self.form_layout.addWidget(self.last_name_input)
        self.form_layout.addWidget(self.id_label)
        self.form_layout.addWidget(self.id_input)
        self.form_layout.addWidget(self.phone_label)
        self.form_layout.addWidget(self.phone_input)
        self.form_layout.addWidget(self.address_label)
        self.form_layout.addWidget(self.address_input)
        self.form_layout.addWidget(self.add_button)
        
        self.layout.addLayout(self.form_layout)
        
        # Tabla para mostrar el registro de personas
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Primer Nombre", "Apellido", "Cédula", "Teléfono", "Dirección"])
        self.layout.addWidget(self.table)
        
        self.setLayout(self.layout)

    def add_person(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        id_number = self.id_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()
        
        if first_name and last_name and id_number and phone and address:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(first_name))
            self.table.setItem(row_position, 1, QTableWidgetItem(last_name))
            self.table.setItem(row_position, 2, QTableWidgetItem(id_number))
            self.table.setItem(row_position, 3, QTableWidgetItem(phone))
            self.table.setItem(row_position, 4, QTableWidgetItem(address))
            
            # Limpiar los campos de entrada
            self.first_name_input.clear()
            self.last_name_input.clear()
            self.id_input.clear()
            self.phone_input.clear()
            self.address_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PersonRegistryApp()
    window.show()
    sys.exit(app.exec())
