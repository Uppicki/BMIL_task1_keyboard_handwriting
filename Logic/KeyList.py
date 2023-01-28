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
