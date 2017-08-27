import re
import operator

from datetime import datetime
from tinydb import TinyDB, Query
from functools import reduce


def is_phone(value: str) -> bool:
    """
    Функция проверяет, является ли переданная строка номером телефона.
    Формат номера телефона, по условию тестового задания: +7 xxx xxx xx xx
    """
    pattern = re.compile("^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$")
    return bool(pattern.match(value))


def is_email(value: str) -> bool:
    """
    Функция проверяет, является ли переданная строка email адресом.
    """
    pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return bool(pattern.match(value))


def is_date(value: str) -> bool:
    """
    Функция проверяет, является ли переданная строка датой по своему формату.
    Формат даты, по условию тестового задания, может быть DD.MM.YYYY или YYYY-MM-DD.
    """

    ddmmyyyy = re.compile("^\d{2}.\d{2}.\d{4}$")  # DD.MM.YYYY
    yyyymmdd = re.compile("^\d{4}-\d{2}-\d{2}$")  # YYYY-MM-DD

    try:
        if ddmmyyyy.match(value):
            datetime.strptime(value, '%d.%m.%Y')
        elif yyyymmdd.match(value):
            datetime.strptime(value, '%Y-%m-%d')
        else:
            raise ValueError()
    except:
        # Неправильный формат даты.
        return False
    else:
        return True


def get_field_type_by_field_value(value: str) -> str:
    """
    Функция возвращает тип поля формы исходя из его значения.
    Всего поддерживается четыре типа полей: date, phone, email, text.
    Тип поля формы 'text' является запасным, когда значение поля формы не совпадает ни с одним из вышеописанных типов.
    """
    if is_date(value):
        return 'date'
    elif is_phone(value):
        return 'phone'
    elif is_email(value):
        return 'email'
    else:
        return 'text'


def search_form_template_name_by_post_parameters(search_params: dict):
    """
    Функция поиска имени шаблона формы.
    Совпавшими считаются поля, у которых совпали имя и тип значения.
    """
    db = TinyDB('db.json')
    q = Query()

    # Первым действием необходиом получить все шаблоны форм,
    # поля которого совпали, хотябы один раз, с полями присланной формы
    query_conditions = [q[field_name] == field_type for field_name, field_type in search_params.items()]
    query = reduce(operator.or_, query_conditions)
    search_result = db.search(query)

    if len(search_result) == 0:
        # Если ни одного шаблона формы не найдено
        return None

    elif len(search_result) == 1:
        # Если был найдет один шаблон формы,
        # значит один или более полей формы совпали,
        # в этом случае возвращаем имя шаблона формы
        return search_result[0]['ftname']

    else:
        # Если найдено больше одного шаблона формы, сравниваем каждый найденый шаблон формы
        # с  полями присланой формы, считаем количество совпавших полей и записываем в словарь.
        # {id шаблона формы: кол-во совпавших полей, ...}
        result = {item.eid: len(set(item.items() & search_params.items())) for item in search_result}

        # Получаем id шаблона формы с максимальным кол-вом совпавших полей ...
        eid = max(result, key=result.get)

        # ... находим его в бд и получаем имя
        return db.get(eid=eid)['ftname']
