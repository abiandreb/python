import register_module as r
import validation as val
import user as u

user_db = [{'login': 'admin', 'password': 'admin1', 'role': 'a'}]


def registration_procedure():
    print('Please type login.')
    user_login = input('Login: ')

    print('Please type password.')
    user_pass = input('Password: ')

    try:
        if not val.no_invalid_char(user_input) and not val.valid_password(user_pass):
            raise TypeError

    except TypeError:
        print('Invalid input')
        return False

    reg = r.Registration(user_login, user_pass, user_db)

    if reg.is_unique_login():
        reg.run()
        print('Successfully registered')

    else:
        print('Login is not unique')


print('My Social network \n')

while True:

    print('Main menu: \n'
          '\n "1" - to sign up \n '
          '\n "2" - to login \n ')

    user_input = input('Type preferable option: ')

    if user_input == '1':
        registration_procedure()

    if user_input == '2':
        print('Please type login.')
        user_login = input('Login: ')

        print('Please type password.')
        user_pass = input('Password: ')

        try:
            if not val.no_invalid_char(user_input) and not val.valid_password(user_pass):
                raise TypeError

        except TypeError:
            print('Invalid input')
            break

        auth = r.Authentication(user_login, user_pass, user_db)

        if auth.is_registered():
            print('No such login')
            break

        if auth.valid_pass() and not auth.is_admin():
            user = u.User(auth.user_index, user_db)
            print('Logged in as a default user')

            while True:
                print('User menu: \n'
                      '1 - add post '
                      '2 - logout'
                      )
                user_choose = input('Type preferable option: ')
                if user_choose == '1':
                    user.add_post()

                if user_choose == '2':
                    break

        if auth.valid_pass() and auth.is_admin():
            admin = u.Admin(auth.user_index, user_db)
            print('Logged in as admin')

            while True:
                print('User menu: \n'
                      '1 - view db '
                      '2 - logout'
                      )
                user_choose = input('Type preferable option: ')
                if user_choose == '1':
                    admin.display_db()

                if user_choose == '2':
                    break
