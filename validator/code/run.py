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
        data['file_name'] = file
        conditions.append(data)

    file_path = "/tmp/organizations/organization.json"
    company_data = json_reader(file_path)
    company = Company(company_data)

    validator = ValidationRules(company)

    return company, conditions, validator


if __name__ == "__main__":
    company, conditions, v = get_prev_data()

    for condition in conditions:
        print(f"Validate condition: {condition['file_name']}")
        res = v.validate(condition)
        print(f"Result of validation: {res}\n\n")
