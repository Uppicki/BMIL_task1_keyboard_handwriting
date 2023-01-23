from PyQt6.QtWidgets import QVBoxLayout

from BMIL_task1_keyboard_handwriting.UI.Components.InputArea import InputArea


class LeftUpperBox(QVBoxLayout):

    def __init__(self):
        super().__init__()

        password1_input_area = InputArea()
        password2_input_area = InputArea()

        self.addWidget(password1_input_area)
        self.addWidget(password2_input_area)




