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

    def add_habit_name(self, habit_name: str) -> None:
        if habit_name not in self.__data.keys():
            self.__data[habit_name] = []

    def add_habit_data(self, habit_name : str, habit_dates: list) -> None:
            try:
                dates = self.__data[habit_name]
                for date in habit_dates:
                    if date not in dates:
                        dates.append(date)
                self.__data[habit_name] = dates
            except KeyError:
                self.__data[habit_name] = dates

    # For test purposes
    def is_empty(self) -> bool:
        return len(self.__data) == 0