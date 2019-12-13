"""
    Модуль с полезными утилитами
"""


class Company:

    def __init__(self, data):
        self.values = data
        print(f"[ Company ] Values: {self.values}")

    def __getitem__(self, key):
        if key == "":
            return None
        elif "." not in key:
            return self.values[key]
        else:
            items_list = key.split('.')
            return self.recursive_value(self.values, items_list)

    def recursive_value(self, dct, items_list):
        if len(items_list) > 1:
            item = items_list.pop(0)
            return self.recursive_value(dct[item], items_list)
        else:
            return dct[items_list[0]]
