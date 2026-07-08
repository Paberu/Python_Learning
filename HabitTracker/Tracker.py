from datetime import date

import rich
import click


from Storage import Storage

class Tracker:

    def __init__(self):
        self.__storage = Storage()

    # CRUD - create, read, update, delete
    # Create
    def add_habit_name(self, habit_name):
        self.__storage.add_habit_name(habit_name)

    def set_habit_date(self, habit_name, habit_date):
        self.__storage.add_habit_data(habit_name, [habit_date])

    def check_habit_today(self, habit_name):
        self.set_habit_date(habit_name, date.today().strftime("%Y-%m-%d"))

    # Read
    def get_habits_names(self):
        return self.__storage.get_habits_names()

    def get_habit_dates(self, habit_name):
        return self.__storage.get_habit_dates(habit_name)



    def save_habits(self):
        self.__storage.save_habits()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tracker = Tracker()
    tracker.add_habit_name('Спорт')
    tracker.set_habit_date('Спорт', '2026-07-06')
    tracker.set_habit_date('Спорт', '2026-07-07')
    tracker.check_habit_today('Спорт')
    tracker.save_habits()