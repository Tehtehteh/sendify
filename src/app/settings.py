import os
import logging

from copy import deepcopy


logger = logging.getLogger('application')


async def create_settings():
    return Settings.from_defaults()


class Settings(object):

    _defaults = {
        'app': {
            'port': 8080,
        },
        'db': {
            'host': 'localhost',
            'user': 'sendify',
            'password': '',
            'database': 'sendify'
        }
    }

    def __init__(self, settings_dict):
        self.settings_dict = deepcopy(self._defaults)
        self.settings_dict.update(settings_dict)

    @classmethod
    def from_defaults(cls):
        return cls(cls._defaults)

    @classmethod
    def from_file(cls, path):
        if not os.path.exists(path):
            logging.warning('Configuration file %s not found. Using system defaults.')
            return cls.from_defaults()
        _, ext = os.path.splitext(path)
        if ext in ('.yml', '.yaml'):
            import yaml
            with open(path) as file_handler:
                settings_dict = yaml.load(file_handler)
                return cls(settings_dict)
        if ext in ('.cfg', '.ini'):
            import configparser
            cfg = configparser.ConfigParser(allow_no_value=True)
            cfg.read(path)
            return cls(cfg._sections)
