from PyQt6.QtWidgets import QApplication, QWidget

from BMIL_task1_keyboard_handwriting.UI.Components.MainWindow import MainWindow


class Application(QApplication):

    def __init__(self):
        super().__init__([])



        self.main_window = MainWindow()



        self.main_window.confirm_button.clicked.connect(self.confirm_password)




        self.main_window.show()

    def confirm_password(self):
        print(self.main_window.left_upper_layout.password1_content_box_is_visible)

        self.main_window.left_upper_layout.password1_content_box_is_visible =\
            not self.main_window.left_upper_layout.password1_content_box_is_visible

        self.main_window.left_upper_layout.__fill__()

        self.main_window.left_upper_layout.password1_area.setWindowModified (True)
        print(self.main_window.left_upper_layout.password1_area.isWindowModified())
        self.main_window.update()
