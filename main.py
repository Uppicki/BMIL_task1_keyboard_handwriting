import keyboard as keyboard

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from BMIL_task1_keyboard_handwriting.UI.Application import Application
from BMIL_task1_keyboard_handwriting.CI.Application import Application as ConsoleApplication


def main_func():
    # Use a breakpoint in the code line below to debug your script.
    while True:
        print("Input your message :")  # Press Ctrl+F8 to toggle the breakpoint.

        record_message = keyboard.record('enter')

        record_message.pop()
        print()
        keyboard.play(record_message)

        print()

        data = Key_List(record_message)


        file = open("input", 'w')

        file.write(str(data))

        file.close()








class Key_List:

    def __init__(self, event_list=[]):
        #Исходный список нажатий
        self.event_list = event_list
        #Конечный список KeyEvent
        #name
        #time down
        #time up
        self.clicked_keys = []

        self.validate_data()



        print("Key list was created")


    def __str__(self):
        result = f'Length of list: {str(len(self.clicked_keys))}:\n'
        for el in self.clicked_keys:
            result += f'\nKey name: {el.name}\n' \
                      f'Time down: {str(el.time_down)}\n' \
                      f'Time up: {str(el.time_up)}\n' \
                      f'Time pressed: {str(el.time_up - el.time_down)}\n'
        return result

    def validate_data(self):
        down_keys = []

        for event in self.event_list:

            if event.event_type == 'down':
                if is_contain(down_keys, event):
                    prev_event = down_keys.pop(get_index(down_keys, event))
                    self.clicked_keys.append(
                        KeyEvent(
                        event.name,
                        prev_event.time,
                        event.time
                    ))

                down_keys.append(event)
            else:
                prev_event = down_keys.pop(get_index(down_keys, event))
                self.clicked_keys.append(KeyEvent(
                    event.name,
                    prev_event.time,
                    event.time
                ))


def get_index(collection, element):
    ind = 0
    for el in collection:
        if el.name == element.name:
            return ind
        else:
            ind += 1
    return -1

def is_contain(collection, element):
    for el in collection:
        if el.name == element.name:
            return True
    return False




class KeyEvent:

    def __init__(self, name, time_down, time_up):
        self.name = name
        self.time_down = time_down
        self.time_up = time_up

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Time down: {self.time_down}\n'




def gui_application():
    app = Application()
    app.exec()


CURRENT_PASSWORD = ""
CONSOLE_MESSAGE_CHANGE_ACTION = "Change action:\n" \
                                "\n1) Input new password"

def console_application():
    app = ConsoleApplication()
    app.start()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    console_application()
    #main_func()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
