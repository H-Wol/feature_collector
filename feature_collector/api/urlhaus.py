import os
from api.config.config import ConfigMgr
from api.api import API


class URLHaus(API):
    def __init__(self):
        self.url = "https://urlhaus-api.abuse.ch/v1/"
        self.config = ConfigMgr().get_instance()

    def get_task_info(self, datas: dict, group_name: str):
        task_info = list()
        keys = datas.keys()
        self.save_dir = self.config.get_config2("DIR", "save_dir")
        self.save_dir = os.path.join(self.save_dir, group_name)
        os.makedirs(self.save_dir, exist_ok=True)

        hashs = ["MD5", "SHA-256"]
        hosts = ["IPs", "Domains"]
        for key in keys:
            if key == "SHA-1":
                continue
            if key in hashs:
                for data in datas[key]:
                    task_info.append(self.get_hash_info(data, key))
            elif key == "URLs":
                for data in datas[key]:
                    task_info.append(self.get_url_info(data))
            elif key in hosts:
                for data in datas[key]:
                    task_info.append(self.get_domain_or_ip_info(data))
        return task_info

    def get_hash_info(self, str, type):
        task_info = super().get_default_dict()
        task_info["type"] = "POST"
        task_info["url"] = self.url + "payload/"
        task_info["save_dir"] = self.get_save_dir(str)
        if type == "MD5":
            task_info["data"] = {"md5_hash": str}
        elif type == "SHA-256":
            task_info["data"] = {"sha256_hash": str}
        return task_info

    def get_url_info(self, str: str):
        task_info = super().get_default_dict()
        task_info["type"] = "POST"
        task_info["url"] = self.url + "url/"
        converted_url = super().get_converted_url(str)
        task_info["save_dir"] = self.get_save_dir(converted_url)
        task_info["data"] = {"url": str}
        return task_info

    def get_domain_or_ip_info(self, str):
        task_info = super().get_default_dict()
        task_info["type"] = "POST"
        task_info["url"] = self.url + "host/"
        task_info["save_dir"] = self.get_save_dir(str)
        task_info["data"] = {"host": str}
        return task_info

    def get_save_dir(self, str):
        return os.path.join(self.save_dir, "{}_URLhaus.json".format(str))
