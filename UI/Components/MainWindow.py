from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

from BMIL_task1_keyboard_handwriting.UI.Components.LeftUpperBox import LeftUpperBox


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keyboard handwriting")

        self.layout = QVBoxLayout()

        upper_layout = QHBoxLayout()

        left_upper_layout = LeftUpperBox()





        upper_layout.addLayout(left_upper_layout)
        upper_layout.addWidget(QLabel("right upper"))

        self.layout.addLayout(upper_layout)
        self.layout.addWidget(QLabel("down"))

        self.setLayout(self.layout)
