from requests import HTTPError

from API.apps import Auth, Users, Authors, Books

if __name__ == '__main__':
    try:
        print(Users.get_user_type())
        Auth.login('vovan', 'sweetpie')
        print('Вы залогинились')
        print(Users.get_my_books())
        print('Ваши данные')
        print(Users.current())
        print(Books.get_all())
        print(Books.get_detail(Books.get_all()[0]['slug']))
        print(Authors.get_all())
        print(Authors.get_detail('mark-lutts'))
        Auth.logout()
        print('Вы разлогинились')

    except HTTPError as err:
        if err.response.status_code == 401:
            print('Вы не авторизованы!')
        else:
            print('Неожиданная http ошибка!')
            print(err)
            print(err.response.json())

