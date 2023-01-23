from PyQt6.QtWidgets import QVBoxLayout, QPushButton


class RightUpperBox(QVBoxLayout):

    def __init__(self):
        super().__init__()

        self.press_button = QPushButton("press")

        self.addWidget(self.press_button)





