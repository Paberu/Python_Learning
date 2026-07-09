import os
from datetime import timedelta, date

from rich.console import Console
from rich.style import Style
from rich.text import Text


class Graphics:
    def __init__(self):
        self.console = Console()

    def show_heatmap(self, habit_dict):
        os.system('cls' if os.name == 'nt' else 'clear')
        days = [date.today() - timedelta(days=i) for i in range(29, -1, -1)]
        habit_column_width = max(len(habit_name) for habit_name in habit_dict) + 2

        # Header for table
        header = Text(' ' * habit_column_width)
        for i, day in enumerate(days):
            if i % 10 == 0:
                date_mark = day.strftime('%d') + '.' + day.strftime('%m')
                header.append(f"{date_mark:<20}")
        header.append(f"{date.today().strftime('%d') + '.' + date.today().strftime('%m')}")
        self.console.print(header)

        # Styles for habit tracking
        done = Style(color='green')
        missed = Style(color='grey37')

        # Filling calendar with colors
        for habit, dates in habit_dict.items():
            row = Text(habit.ljust(habit_column_width))
            for day in days:
                day = day.strftime('%Y-%m-%d')
                if day in dates:
                    row.append('██', style=done)
                else:
                    row.append('██', style=missed)
            self.console.print(row)

if __name__ == '__main__':
    graphics = Graphics()
    test_data = {'Пианино':['2026-07-01', '2026-07-02', '2026-07-04', '2026-07-07'],
                 'Заполнение дневника (в вечернее время)':['2026-06-25', '2026-06-26', '2026-06-29', '2026-06-30','2026-07-01', '2026-07-02', '2026-07-03', '2026-07-04','2026-07-05', '2026-07-06', '2026-07-07', '2026-07-08']}
    graphics.show_heatmap(test_data)