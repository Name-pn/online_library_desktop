from requests import HTTPError

from API.apps import Auth, Users

if __name__ == '__main__':
    try:
        Auth.login('vovan', 'sweetpie')
        print('Вы залогинились')

        print('Ваши данные')
        print(Users.current())

        Auth.logout()
        print('Вы разлогинились')

    except HTTPError as err:
        if err.response.status_code == 401:
            print('Вы не авторизованы!')
        else:
            print('Неожиданная http ошибка!')
            print(err)
            print(err.response.json())

