"""
Создает файл с тестовой базой, содержащий шаблоны форм.
"""

from tinydb import TinyDB

if __name__ == '__main__':
    db = TinyDB('db.json')
    db.purge()
    db.insert({'ftname': 'OrderForm', 'user_name': 'text', 'order_date': 'date', 'user_email': 'email'})
    db.insert({'ftname': 'BatmanForm', 'first_name': 'text', 'age': 'text', 'birth_date': 'date'})
    db.insert({'ftname': 'ContactForm', 'user_name': 'text', 'user_email': 'email', 'user_phone': 'phone'})