import os
from api.api import API
from api.config.config import ConfigMgr


class OTX(API):
    def __init__(self):
        self.url = "https://otx.alienvault.com/api/v1/indicators/"
        self.config = ConfigMgr().get_instance()

    def get_task_info(self, datas: dict, group_name: str):
        task_info = list()
        keys = datas.keys()
        self.save_dir = self.config.get_config2("DIR", "save_dir")
        key = self.config.get_config2("KEY", "otx_api_key")
        self.save_dir = os.path.join(self.save_dir, group_name)
        self.header = {
            'X-OTX-API-KEY': key,
        } # API KEY 설정
        os.makedirs(self.save_dir, exist_ok=True)

        hashs = ["MD5", "SHA-256", "SHA-1"]
        for key in keys:
            if key in hashs:
                for data in datas[key]:
                    task_info = task_info + self.get_hash_info(data)
            elif key == "URLs":
                for data in datas[key]:
                    task_info = task_info + self.get_url_info(data)
            elif key == "IPs":
                for data in datas[key]:
                    task_info = task_info + self.get_ip_info(data)
            elif key == "Domains":
                for data in datas[key]:
                    task_info = task_info + self.get_domain_info(data)
            else:
                pass
        return task_info

    def get_hash_info(self, str):
        """
        파일 Hash 정보 관련 API
        """
        task_infos = list()
        sections = ["general", "analysis"]
        for section in sections:
            task_info = super().get_default_dict()
            task_info["header"] = self.header
            task_info["type"] = "GET"
            task_info["url"] = self.url + "file/{}/{}".format(str, section)
            task_info["save_dir"] = self.get_save_dir(str, section)
            task_infos.append(task_info)
        return task_infos

    def get_url_info(self, str: str):
        """
        URL 관련 API
        """
        task_infos = list()
        sections = ["general", "url_list"]
        for section in sections:
            task_info = super().get_default_dict()
            task_info["header"] = self.header
            task_info["type"] = "GET"
            task_info["url"] = self.url + "url/{}/{}".format(str, section)
            converted_url = super().get_converted_url(str)
            task_info["save_dir"] = self.get_save_dir(converted_url, section) #URL 데이터의 / 와 \ 를 _로 치환
            task_infos.append(task_info)
        return task_infos

    def get_domain_info(self, str: str):
        """
        도메인 관련 API
        """
        task_infos = list()
        sections = ["general", "geo", "malware", "url_list",
                    "passive_dns", "whois", "http_scans"]
        for section in sections:
            task_info = super().get_default_dict()
            task_info["header"] = self.header
            task_info["type"] = "GET"
            task_info["url"] = self.url + "domain/{}/{}".format(str, section)
            task_info["save_dir"] = self.get_save_dir(str, section)
            task_infos.append(task_info)
        return task_infos

    def get_ip_info(self, str: str):
        """
        IP 관련 API
        """
        task_infos = list()
        # IPv4
        sections = ["general", "reputation", "geo", "malware",
                    "url_list", "passive_dns", "http_scans"]
        # IPv6
        # sections = ["general", "reputation", "geo", "malware",
        #             "url_list", "passive_dns"]

        for section in sections:
            task_info = super().get_default_dict()
            task_info["header"] = self.header
            task_info["type"] = "GET"
            task_info["url"] = self.url + "IPv4/{}/{}".format(str, section)
            task_info["save_dir"] = self.get_save_dir(str, section)
            task_infos.append(task_info)
        return task_infos

    def get_save_dir(self, str, section):
        return os.path.join(self.save_dir, "{}_OTX_{}.json".format(str, section))
