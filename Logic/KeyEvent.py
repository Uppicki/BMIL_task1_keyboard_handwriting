class KeyEvent:

    def __init__(self, name, time_down, time_up):
        self.name = name
        self.time_down = time_down
        self.time_up = time_up

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Time down: {self.time_down}\n'