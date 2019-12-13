"""
    Точка входа в приложение
"""
import os
from filehadler import json_reader
from tools import Company, ValidationRules


def get_prev_data():
    """
    Собирает необходимые данные для запуска программы

    :argument: Nothing

    :return: company (dict) - данные по проверяемой организации
             conditions (list) - список, содержащий словари правил валидации
    """
    conditions = []
    dir_path = "/tmp/conditions/"
    for file in os.listdir(path=dir_path):
        data = json_reader(dir_path+file)
        conditions.append(data)

    file_path = "/tmp/organizations/organization.json"
    company_data = json_reader(file_path)
    company = Company(company_data)

    return company, conditions


if __name__ == "__main__":
    company, conditions = get_prev_data()

    v = ValidationRules(company)

    for condition in conditions:
        print(f"Validate condition: {condition}")
        res = v.validate(condition)
        print(f"Result of validate = {res}\n\n")