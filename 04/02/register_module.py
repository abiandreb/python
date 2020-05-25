from datetime import datetime


class Registration:

    def __init__(self, login, password, db):
        self._login = login
        self._password = password
        self._db = db

    def is_unique_login(self):
        res = 1
        for i in self._db:
            if i['login'] == self._login:
                res = 0
                break

        if res == 1:
            return True

        else:
            return False

    def run(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        self._db.append(
            {
                'login': self._login,
                'password': self._password,
                'role': 'u',
                'registration': date_time

            }
        )


class Authentication(Registration):
    user_index = None

    def is_registered(self):

        for i in self._db:
            if i['login'] == self._login:
                self.user_index = self._db.index(i)
                break
        if self.user_index is None:
            return False

    def valid_pass(self):
        if self._db[self.user_index]['password'] == self._password:
            return True

    def is_admin(self):
        if self._db[self.user_index]['role'] == 'a':
            return True
