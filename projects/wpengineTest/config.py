import json

"""
Responsible for loading data from json based config file
"""


class Config:
    def __init__(self, config_file):
        with open(config_file, encoding='utf-8') as file:
            data = json.load(file)
            self.user = data['user']
            self.password = data['password']
            self.driver_path = data['driver_path']
