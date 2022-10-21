import os
import logging
import configparser
from datetime import datetime


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
            self.config.read(self.config_file)
        except Exception as e:
            raise e

    def get_config(self, name):
        try:
            return self.config[name]
        except KeyError:
            err_msg = f"set the {name} enviroment variable"
            raise err_msg

    def get_config2(self, name, name2):
        try:
            return self.config[name][name2]
        except KeyError:
            err_msg = f"set the {name}/{name2} enviroment variable"
            raise err_msg

    def get_tried_cnt(self):
        try:
            now_tried_cnt = int(self.config["VT_VALUE"]["tried"])
            config_date = self.config["VT_VALUE"]["config_date"]
            today = datetime.utcnow().strftime('%Y-%m-%d')
            if config_date != today:
                self.config["VT_VALUE"]["tried"] = str(1)
                self.config["VT_VALUE"]["config_date"] = today
                return 1
            now_tried_cnt = now_tried_cnt + 1
            self.config["VT_VALUE"]["tried"] = str(now_tried_cnt)
            with open(self.config_file, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
            return now_tried_cnt
        except Exception as e:
            err_msg = f"set the VT_VALUE enviroment variable"
            raise err_msg
