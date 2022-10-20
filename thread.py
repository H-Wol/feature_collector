import json
import logging
import requests


class Thread:
    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.header = {
            "Content-Type": "application/json"
        }

    def __call__(self, type: str, url: str, header: dict, data: dict, save_dir: str):
        try:
            self.header.update(header)
            return_dict = dict()
            if type == "POST":
                return_dict = self.post(url, header, data)
            elif type == "GET":
                return_dict = self.get(url, header)
            self.save_file(return_dict, save_dir)
        except:
            pass

    def get(self, url, header):
        json_data = dict()
        try:
            response = requests.get(url, headers=header, timeout=15)
            json_data = response.json()
        except Exception as e:
            self.logger.error(e)
            json_data["failure"] = str(e)
        finally:
            return json_data

    def post(self, url, header, data):
        json_data = dict()
        try:
            response = requests.post(
                url, headers=header, data=data, timeout=15)
            json_data = response.json()
        except Exception as e:
            self.logger.error(e)
            json_data["failure"] = str(e)
        finally:
            return json_data

    def save_file(self, data, save_dir):
        with open(save_dir, 'w') as fp:
            json.dump(data, fp)
