from PyQt6.QtWidgets import QApplication

from BMIL_task1_keyboard_handwriting.UI.Windows.MainWindow import MainWindow


class Application(QApplication):

    def __init__(self):
        super().__init__([])



        self.main_window = MainWindow()


        self.main_window.show()


