import os
import time
import json
import logging
import requests
from api.config.config import ConfigMgr
from api.api import API
from threading import Thread
import traceback


class VTApi(API):
    def __init__(self):
        self.logger = logging.getLogger()
        self.url = "https://www.virustotal.com/api/v3/"
        self.headers = {"accept": "application/json"}
        self.config = ConfigMgr().get_instance()
        self.headers["x-apikey"] = self.config.get_config2("KEY", "vt_api_key")
        self.delay_rate = int(self.config.get_config2("VT_VALUE", "rate")) # 각 요청마다 딜레이 설정
        self.started = False # 요청간 딜레이를 처음 실행에는 실행하지 않기 위한 변수

    def thread_run(self, datas: dict, group_name: str):
        th = Thread(target=self.get_info, args=(datas, group_name)) # Thread를 생성하여 백그라운드로 실행
        # th.daemon = True
        th.start()

    def get_info(self, datas: dict, group_name: str):
        try:
            keys = datas.keys()
            self.save_dir = self.config.get_config2("DIR", "save_dir")
            self.save_dir = os.path.join(self.save_dir, group_name)
            os.makedirs(self.save_dir, exist_ok=True)

            hashs = ["MD5", "SHA-256", "SHA-1"]
            for key in keys:
                if key in hashs:
                    for data in datas[key]:
                        self.get_hash_info(data)
                elif key == "URLs":
                    for data in datas[key]:
                        self.get_url_info(data)
                elif key == "IPs":
                    for data in datas[key]:
                        self.get_ip_info(data)
                elif key == "Domains":
                    for data in datas[key]:
                        self.get_domain_info(data)
        except:
            self.logger.error(traceback.format_exc())

    def check_max_vt_reqeust_times(self):
        try:
            tried_time = self.config.get_tried_cnt()
            if tried_time >= int(self.config.get_config2("VT_VALUE", "max_try")): # 일일 최대 요청 건수가 기준을 넘었을 경우
                err_msg = "The number of requests has been exceeded."
                self.logger.error(err_msg)
                json_data = dict()
                json_data["failure"] = err_msg
                return json_data
            self.delay()
            return False
        except:
            self.logger.error(traceback.format_exc())

    def get_hash_info(self, str):
        """
        파일 Hash 정보 관련 API
        """
        json_data = dict()
        try:
            check = self.check_max_vt_reqeust_times()
            if check:
                json_data = check
                return
            request_url = self.url + "files/" + str
            response = requests.get(
                request_url, headers=self.headers, timeout=15)
            json_data = response.json()
            return
        except Exception as e:
            self.logger.error(e)
            json_data["failure"] = str(e)
            return
        finally:
            self.save_file(json_data, str)

    def get_url_info(self, str):
        """
        URL 관련 API
        """
        json_data = dict()
        try:
            check = self.check_max_vt_reqeust_times()
            if check:
                json_data = check
                return
            request_url = self.url + "urls/" + str
            response = requests.get(
                request_url, headers=self.headers, timeout=15)
            json_data = response.json()
            converted_url = super().get_converted_url(str) #URL 데이터의 / 와 \ 를 _로 치환
            return
        except Exception as e:
            self.logger.error(e)
            json_data["failure"] = str(e)
            return
        finally:
            self.save_file(json_data, converted_url)

    def get_ip_info(self, str):
        """
        IP 관련 API
        """
        json_data = dict()
        try:
            check = self.check_max_vt_reqeust_times()
            if check:
                json_data = check
                return
            request_url = self.url + "ip_addresses/" + str
            response = requests.get(
                request_url, headers=self.headers, timeout=15)
            json_data = response.json()
            return
        except Exception as e:
            self.logger.error(e)
            json_data["failure"] = str(e)
            return
        finally:
            self.save_file(json_data, str)

    def get_domain_info(self, str):
        """
        Domain 관련 API
        """
        json_data = dict()
        try:
            check = self.check_max_vt_reqeust_times()
            if check:
                json_data = check
                return
            request_url = self.url + "domains/" + str
            response = requests.get(
                request_url, headers=self.headers, timeout=15)
            json_data = response.json()
            return
        except Exception as e:
            self.logger.error(e)
            json_data["failure"] = str(e)
            return
        finally:
            self.save_file(json_data, str)

    def save_file(self, data, filename):
        with open(os.path.join(self.save_dir, '{}_{}.json'.format(filename, "VirusTotal")), 'w') as fp:
            json.dump(data, fp)

    def delay(self):
        if self.started: #처음 실행된 경우가 아닌 경우
            time.sleep(self.delay_rate) #설정된 시간만큼 딜레이
        else:
            self.started = True 
