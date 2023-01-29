from BMIL_task1_keyboard_handwriting.Logic.KeyList import KeyList

import matplotlib.pyplot as plt
import numpy as np

class Experience:

    def __init__(self, start_datetime):
        self.key_list = KeyList()
        self.start_datetime = start_datetime
        self.end_datetime = 0

    def clear(self):
        return

    def fill(self, record_message, end_datetime):
        self.key_list.fill(record_message)
        self.key_list.validate_data()
        self.end_datetime = end_datetime

    def analyze(self):
        pass

    def graph(self):
        ox = np.arange(
            self.start_datetime,
            self.end_datetime,
            0.001
        )

        f = lambda x: [ 0 if x.time_down < i and x.time_up > 0 else x.time_pressed for i in ox]

        for event in self.key_list:
            plt.plot(ox, f(event))

        plt.show()
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')




