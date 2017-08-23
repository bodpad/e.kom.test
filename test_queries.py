"""
Cкрипт совершает три тестовых POST запроса
"""

import requests

if __name__ == '__main__':
    queries = [
        {'first_name': 'Batman', 'age': '35'},
        {'user_name': 'bodpad', 'user_email': 'myqoop@yandex.ru', 'user_phone': '+7 111 111 11 11'},
        {'user_name': 'bodpad', 'order_date': '20.02.1991', 'user_email': 'myqoop@yandex.ru'},
    ]

    for data in queries:
        r = requests.post('http://127.0.0.1:8888/get_form', data=data)
        print(r.text)