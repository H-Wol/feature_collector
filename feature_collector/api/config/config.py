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
        """
        VirusTotal API의 일일 요청 횟수 관련 함수
        """
        try:
            now_tried_cnt = int(self.config["VT_VALUE"]["tried"]) # 요청한 횟수
            print(now_tried_cnt)
            config_date = self.config["VT_VALUE"]["config_date"] # 기준 날짜
            today = datetime.utcnow().strftime('%Y-%m-%d')
            if config_date != today: # 금일이 기준날짜와 다를경우
                self.config["VT_VALUE"]["tried"] = str(1) #요청한 횟수 초기화
                self.config["VT_VALUE"]["config_date"] = today #기준 날짜를 금일로 변경
                return 1
            now_tried_cnt = now_tried_cnt + 1 #요청 횟수 추가
            self.config["VT_VALUE"]["tried"] = str(now_tried_cnt) #요청 횟수 기록
            return now_tried_cnt
        except Exception as e:
            err_msg = f"set the VT_VALUE enviroment variable"
            raise err_msg
        finally:
            with open(self.config_file, 'w', encoding='utf-8') as configfile: # 변경 사항 저장
                self.config.write(configfile)  
