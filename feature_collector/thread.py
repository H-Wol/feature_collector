import json
import logging
import requests
import traceback


class Thread:
    def __init__(self):
        self.logger = logging.getLogger()
        self.header = {
            "Content-Type": "application/json"
        }

    def __call__(self, type: str, url: str, header: dict, data: dict, save_dir: str):
        try:
            self.header.update(header) # 헤더 추가 정보가 있을 경우 추가되고 기존 데이터는 덮어 씌워짐
            return_dict = dict()
            if type == "POST":
                return_dict = self.post(url, header, data)
            elif type == "GET":
                return_dict = self.get(url, header)
            self.save_file(return_dict, save_dir)
        except:
            self.logger.error(traceback.format_exc())

    def get(self, url, header):
        json_data = dict()
        try:
            response = requests.get(url, headers=header, timeout=15)
            json_data = response.json()
        except Exception as e:
            # self.logger.error(e)
            self.logger.error(url)
            self.logger.error(traceback.format_exc())
            json_data["failure"] = str(e) # API 요청이 실패할 경우 에러 메시지로 데이터 생성
        finally:
            return json_data

    def post(self, url, header, data):
        json_data = dict()
        try:
            response = requests.post(
                url, headers=header, data=data, timeout=15)
            json_data = response.json()
        except Exception as e:
            # self.logger.error(e)
            self.logger.error(traceback.format_exc())
            json_data["failure"] = str(e) # API 요청이 실패할 경우 에러 메시지로 데이터 생성
        finally:
            return json_data

    def save_file(self, data, save_dir):
        with open(save_dir, 'w') as fp:
            json.dump(data, fp)
