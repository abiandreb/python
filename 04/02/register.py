import re


class Register:

    def __init__(self, name, login, password, db, role='u'):
        self._name = name
        self._login = login
        self._password = password
        self._db = db
        self._role = role

    def validate_password(self):
        reg = re.compile(r"^[^<>/{}[\]~`]*$")

        def has_numbers(input_string):
            return bool(re.search(r'\d', input_string))

        if reg.match(self._password) and not has_numbers(self._password):
            return False

        else:
            return True

    def validate_name(self):
        try:
            if not self._name.isalpha():
                raise TypeError

        except TypeError:
            print('Invalid name format')

    def validate_login(self):
        reg = re.compile(r"^[^<>/{}[\]~`]*$")
        try:
            if reg.match(self._login):
                raise TypeError

        except TypeError:
            print('Invalid Login Format')

    def is_unique_login(self):
        check = 1
        for i in self._db:
            if i['login'] == self._login:
                check = 0
                break

        if check == 0:
            return False
        else:
            return True

    def register(self):
        return self._db.append({

            'name': self._name,
            'login': self._login,
            'password': self._password,
            'role': self._role,
            'posts': []

        })

    def __call__(self, *args, **kwargs):
        if self.validate_login() and self.validate_password() and self.validate_name() and self.is_unique_login():
            self.register()


class Authenticate(Register):

