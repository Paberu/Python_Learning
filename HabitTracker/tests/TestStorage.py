import unittest

from Storage import Storage


class StorageTest(unittest.TestCase):

    def setUp(self):
        self.storage = Storage()

    def test_load_habits(self):
        self.storage.load_habits()
        self.assertFalse(self.storage.is_empty())

    def test_save_habits(self):
        self.storage.save_habits()
        self.assertFalse(self.storage.is_empty())

    def test_check_habits(self):
        self.assertFalse(self.storage.check_habit('Спорт'))

    def test_add_habit_data(self):
        self.storage.add_habit_data('Спорт',['2026-06-05', '2026-06-06'])
        self.assertTrue(self.storage.check_habit('Спорт'))

    def test_add_habit_name(self):
        self.storage.add_habit_name('Спорт')
        self.assertTrue(self.storage.check_habit('Спорт'))

    def test_get_habit_names(self):
        self.storage.add_habit_data('Спорт', ['2026-06-05', '2026-06-06'])
        self.assertEqual(self.storage.get_habit_names(), ['Спорт'])

    def test_get_habit_dates(self):
        self.storage.add_habit_data('Спорт', ['2026-06-05', '2026-06-06'])
        self.assertEqual(self.storage.get_habit_dates('Спорт'), ['2026-06-05', '2026-06-06'])