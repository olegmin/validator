"""
    Точка входа в приложение
"""
import os
from filehadler import json_reader


if __name__ == "__main__":
    dir_path = "/tmp/conditions/"
    for file in os.listdir(path=dir_path):
        data = json_reader(dir_path+file)
        print(f"\n{data}\n\ttype:{type(data)}\n")
