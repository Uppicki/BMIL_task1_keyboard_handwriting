from PyQt6.QtWidgets import QVBoxLayout, QLabel

from BMIL_task1_keyboard_handwriting.UI.Components.InputArea import InputArea


class LeftUpperBox(QVBoxLayout):

    def __init__(self):
        super().__init__()

        self.password1_input_area = InputArea()
        self.password1_label_area = QLabel('Input')

        self.password1_content_box_is_visible = False

        self.__fill__()

        self.password2_input_area = InputArea()

        self.addWidget(self.password1_area)
        self.addWidget(self.password2_input_area)

    def __fill__(self):
        if self.password1_content_box_is_visible:
            self.password1_area = self.password1_input_area
        else:
            self.password1_area = self.password1_label_area

        self.update()



