import os
from configparser import RawConfigParser

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = os.path.join(os.path.dirname(SCRIPT_PATH), 'mantira.conf')


class Section:
    def __init__(self, params):
        self.__dict__.update(params)


class Config:
    def __init__(self, *file_names):
        parser = RawConfigParser()
        parser.optionxform = str
        found = parser.read(file_names)

        if not found:
            raise ValueError('Config file not found!')

        for name in parser.sections():
            self.__dict__.update([(name, Section(parser.items(name)))])


config = Config(CONFIG_FILE)