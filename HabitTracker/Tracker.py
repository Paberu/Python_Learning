import rich
import click

from Storage import Storage


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    storage = Storage()
    storage.add_habit_data({'Спорт': ['2026-06-05', '2026-06-06']})
    storage.add_habit_data({'Спорт': ['2026-06-05', '2026-06-06']})
    storage.save_habits()