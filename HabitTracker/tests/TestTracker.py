import unittest

from Tracker import Tracker


class TrackerTest(unittest.TestCase):

    def setUp(self):
        self.tracker = Tracker()

    def test_add_habit_name(self):
        self.tracker.add_habit_name('Спорт')
        self.assertEqual(self.tracker.get_habit_names(), ['Спорт',])

    def test_set_habit_date(self):
        self.tracker.set_habit_date('Спорт', '2026-06-05')
        self.assertEqual(self.tracker.get_habit_dates('Спорт'), ['2026-06-05',])

    def test_check_habit_today(self):
        self.tracker.add_habit_name('Спорт')
        self.tracker.check_habit_today('Спорт')
        self.assertEqual(self.tracker.get_habit_dates('Спорт'), ['2026-07-07',])