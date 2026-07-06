import json


class Storage:

    def __init__(self):
        self.__path = 'storage.json'
        self.__data = self.load_habits()  # dict

    def load_habits(self) -> dict:
        try:
            with open(self.__path, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {}

    def save_habits(self) -> None:
        with open(self.__path, 'w', encoding='utf-8') as json_file:
            json.dump(self.__data, json_file, ensure_ascii=False, indent=4)

    def check_habit(self, habit) -> bool:
        return habit in self.__data.keys()

    def add_habit_data(self, habit_data: dict):
        for habit, dates in habit_data.items():
            try:
                habit_dates = self.__data[habit]
                for date in dates:
                    if date not in habit_dates:
                        habit_dates.append(date)
                self.__data[habit] = habit_dates
            except KeyError:
                self.__data[habit] = dates

