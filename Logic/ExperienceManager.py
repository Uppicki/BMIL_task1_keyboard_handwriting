import datetime

import keyboard

from BMIL_task1_keyboard_handwriting.Logic.Experience import Experience


class ExperienceManager:

    def __init__(self):
        return

    def do_experience(self):
        start_time = datetime.datetime.now()
        record_message = keyboard.record('enter')
        record_message.pop()

        exp = Experience(datetime)
        exp.fill(record_message)
        exp.graph()







