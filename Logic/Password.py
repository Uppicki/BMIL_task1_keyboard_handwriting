import string

SYMBOLS_DICT = ('qwertyuiop'
                'asdfghjkl'
                'zxcvbnm'
                '1234567890'
                ' !"\'/{}[];:,.<>?@#$%^&*()_+=-`~')

class Password:

    def __init__(self, password=''):
        print("\nPassword was created\n")

        self.password = password

        self.__validate__()

    def __validate__(self):
        self.errors = []
        password = self.password

        length = (len(password) >= 6)

        upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
        lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])

        special = any([1 if i in string.punctuation else 0 for i in password])
        digits = any([1 if i in string.digits else 0 for i in password])

        repeat = False

        p = password.lower()
        for i in range(len(password) - 3):
            s = p[i:i + 4]
            if s in SYMBOLS_DICT:
                repeat = True
                break


        characters = [length, upper_case, lower_case, special, digits, (not repeat)]

        self.complexity = sum(characters)

        self.is_valid = length and digits and lower_case and upper_case

        if not length:
            self.errors.append('Пароль должен содержать 6 и более символов')
        if not upper_case:
            self.errors.append('Пароль должен содержать буквы верхнего регистра')
        if not lower_case:
            self.errors.append('Пароль должен содержать буквы нижнего регистра')
        if not special:
            self.errors.append('Пароль должен содержать спец. символы')
        if not digits:
            self.errors.append('Пароль должен содержать числа')
        if repeat:
            self.errors.append('Пароль не должен состоять из последовательных символов')


        print(self)

    def __str__(self):
        result = f"Current password: {self.password}\n" \
                 f"Сложность: {self.complexity}/6\n" \
                 f"Валидность: {self.is_valid}\n\n"

        for element in self.errors:
            result += element + '\n'

        return result

