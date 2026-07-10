from datetime import date

import rich
import click

from Graphics import Graphics
from Storage import Storage

class Tracker:

    def __init__(self):
        self.__storage = Storage()
        self.__graphics = Graphics()

    # CRUD - create, read, update, delete
    # Create
    def add_habit_name(self, habit_name):
        self.__storage.add_habit_name(habit_name)

    # Read
    def get_habits_names(self):
        return self.__storage.get_habits_names()

    def get_habit_dates(self, habit_name):
        return self.__storage.get_habit_dates(habit_name)

    # Update
    def set_habit_date(self, habit_name, habit_date):
        self.__storage.add_habit_data(habit_name, [habit_date])

    def check_habit_today(self, habit_name):
        self.set_habit_date(habit_name, date.today().strftime("%Y-%m-%d"))

    # Delete
    def delete_habit(self, habit_name):
        if habit_name in self.get_habits_names():
            self.__storage.delete_habit(habit_name)
    #End of CRUD

    # Control
    def save_habits(self):
        self.__storage.save_habits()

    def display(self):
        self.__graphics.show_heatmap(self.__storage.get_data())


if __name__ == '__main__':
    tracker = Tracker()
    while True:
        tracker.save_habits()
        tracker.display()
        command, parameter = input().split(maxsplit=1)
        command = command.lower()
        if command == 'q' or command == 'quit':
            break
        elif command == 'add':
            tracker.add_habit_name(parameter)
        elif command == 'set':
            name, date = parameter.rsplit(maxsplit=1)
            tracker.set_habit_date(name, date)
        elif command == 'delete':
            tracker.delete_habit(parameter)
