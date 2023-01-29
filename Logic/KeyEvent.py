class KeyEvent:

    def __init__(self, name, time_down, time_up):
        self.name = name
        self.time_down = round(time_down, 3)
        self.time_up = round(time_up, 3)
        self.time_pressed = round(time_up - time_down, 2)

    def __str__(self):
        return f'\nName: {self.name}\n' \
               f'Time down: {self.time_down}\n' \
               f'Time up: {self.time_up}\n' \
               f'Time pressed: {self.time_pressed}\n'

