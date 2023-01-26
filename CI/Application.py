
SYMBOLS_DICT = ('qwertyuiop'
                'asdfghjkl'
                'zxcvbnm'
                '1234567890'
                ' !"\'/{}[];:,.<>?@#$%^&*()_+=-`~')
CONSOLE_MESSAGE_CURRENT_PASSWORD = (lambda x:
                                    f"\nCurrent password: {x}\n")
CONSOLE_MESSAGE_START_MENU = f"\nChange action:\n"\
                              f"1) Input new password\n"\
                              f"2) New experience\n"\
                              f"3) Old experiences\n"
CONSOLE_MESSAGE_INPUT_ERROR = f"\nYou should input int number (1 .. 3)"


class Application:

    def __init__(self):
        print("Console application was created")

        self.password = ''




    def start(self):
        change = 0

        while change >= 0:
            try:
                print(CONSOLE_MESSAGE_CURRENT_PASSWORD("password") +
                        CONSOLE_MESSAGE_START_MENU)

                change = int(input("Input your change: "))

                if change == 1:
                    print("ok")
                elif change == 2:
                    print("ok")
                elif change == 3:
                    print("ok")
                else:
                    print(CONSOLE_MESSAGE_INPUT_ERROR)


            except:
                print(CONSOLE_MESSAGE_INPUT_ERROR)


    def input_password(self):
        print(CONSOLE_MESSAGE_CURRENT_PASSWORD(self.password))

        password = input("\nInput new password")








