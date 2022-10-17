import os
import logging
import configparser


class ConfigMgr:
    
    _instance = None

    def __init__(self):
        self.logger = logging.getLogger()
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.config_file = os.path.join(
            BASE_DIR, 'config/config.ini')
        self.open_config()

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ConfigMgr()
        return cls._instance
    
    def open_config(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.read('config.ini')
        except Exception as e:
            raise e

    def get_config(self, name):
        try:
            return self.config[name]
        except KeyError:
            err_msg = f"set the {name} enviroment variable"
            raise err_msg

    def get_config(self, name, name2):
        try:
            return self.config[name][name2]
        except KeyError:
            err_msg = f"set the {name}/{name2} enviroment variable"
            raise err_msg

