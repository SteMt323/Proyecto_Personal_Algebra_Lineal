from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, 
    QHBoxLayout, QPushButton,
    QLabel, QTableWidget, 
    QTableWidgetItem, QSpinBox,
    QGroupBox, QLineEdit
    )

from PySide6.QtCore import Qt
import numpy as np
import pyqtgraph as pg
from sympy import symbols

from ...core.linear_systems import LinearSystems

class LinearSystemsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        
    # Configuracion de la interfaz para los sistemas lineales #
    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        
        # Controles #
        self.dim_control = QSpinBox()
        self.dim_control.setRange(1, 5)
        self.dim_control.setValue(2)
        dim_layout = QHBoxLayout()
        
        dim_layout.addWidget(QLabel("Numbers of variables: "))
        dim_layout.addWidget(self.dim_control)
        main_layout.addLayout(dim_layout)
        
        