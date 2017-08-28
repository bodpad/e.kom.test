from tornado.web import RequestHandler
import tornado
from utils import *


class MainHandler(RequestHandler):

    def post(self):
        """
        Входные данные - cписок полей формы со значениями
        """
        if bool(self.request.arguments) is False:
            # Возвращаем "Bad Request", если в запросе не передали ни одного аргумента
            raise tornado.web.HTTPError(400)

        # search_params - словарь вида {'field_name': 'field_type', ...},
        # для поиска в бд подходящего шаблона формы.
        search_params = {}

        # Для получения этого словаря, необходимо пройтись по все параметрам POST запроса
        # и получить тип поля на основе его значения. см. реализацию get_field_type_by_field_value()
        for field_name in self.request.arguments:
            field_value = self.get_argument(field_name)
            search_params[field_name] = get_field_type_by_field_value(field_value)

        # Получаем имя шаблона формы по названиям полей формы и их типов
        form_template_name = search_form_template_name_by_post_parameters(search_params)

        if not form_template_name is None:
            # Если шаблон формы был найден, возвращаем его имя.
            self.write(form_template_name)
        else:
            # В противном случае, по условию тестового задания,
            # возвращаем переданные поля формы с их типами вида:
            # field_name1: FIELD_TYPE
            # field_nameN: FIELD_TYPE
            self.write(search_params)