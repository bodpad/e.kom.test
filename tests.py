import unittest
from utils import *


class TestUtils(unittest.TestCase):

    def test_is_phone(self):
        self.assertTrue(is_phone('+7 123 456 78 90'))

    def test_is_email(self):
        self.assertTrue(is_email('example@example.com'))

    def test_is_date(self):
        self.assertTrue(is_date('01.01.2017'))
        self.assertTrue(is_date('2017-01-01'))

    def test_get_field_type_by_field_value(self):
        self.assertEqual(get_field_type_by_field_value('+7 123 456 78 90'), 'phone')
        self.assertEqual(get_field_type_by_field_value('example@example.com'), 'email')
        self.assertEqual(get_field_type_by_field_value('01.01.2017'), 'date')
        self.assertEqual(get_field_type_by_field_value('2017-01-01'), 'date')

if __name__ == '__main__':
    unittest.main()