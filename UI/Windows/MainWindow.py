from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

from BMIL_task1_keyboard_handwriting.UI.Containers.LeftUpperBox import LeftUpperBox
from BMIL_task1_keyboard_handwriting.UI.Containers.RightUpperBox import RightUpperBox


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 400)

        self.setWindowTitle("Keyboard handwriting")

        self.layout = QVBoxLayout()

        self.upper_layout = QHBoxLayout()

        self.left_upper_layout = LeftUpperBox()
        self.right_upper_layout = RightUpperBox()


        self.upper_layout.addLayout(self.left_upper_layout)
        self.upper_layout.addLayout(self.right_upper_layout)

        self.layout.addLayout(self.upper_layout)
        self.layout.addWidget(QLabel("down"))



        self.confirm_button = self.right_upper_layout.press_button

        self.setLayout(self.layout)

        self.confirm_button.clicked.connect(self.confirm_password)


    def confirm_password(self):
        self.left_upper_layout.password1_content_box_is_visible =\
            not self.left_upper_layout.password1_content_box_is_visible

        print(self.left_upper_layout.password1_content_box_is_visible)
        self.layout.update()
