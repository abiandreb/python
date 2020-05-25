from datetime import datetime


class User:

    def __init__(self, index, db):
        self._index = index
        self._db = db

    def add_post(self):
        user_profile = self._db[self._index]
        user_profile['posts'] = []
        post = input('Write your post: ')
        now = datetime.now()
        post_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        data = user_profile['posts']
        data.append((post, post_date))


class Admin(User):

    def display_db(self):
        for i in self._db:
            if i['role'] == 'a':
                continue
            print(f'User login: {i["login"]}, Registered: {i["registration"]}, Posts: {i["posts"]}')
