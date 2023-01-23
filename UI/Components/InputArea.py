from PyQt6.QtWidgets import QLineEdit


class InputArea(QLineEdit):

    def __init__(self, placeholder_text="input"):
        super().__init__()

        self.setPlaceholderText(placeholder_text)
