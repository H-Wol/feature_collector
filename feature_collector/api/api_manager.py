from api.urlhaus import URLHaus
from api.malware_bz import MalwareBazzar
from api.otx import OTX


class ApiManager():
    def __init__(self):
        self.api_list = list()
        self.api_list.append(URLHaus())
        self.api_list.append(MalwareBazzar())
        self.api_list.append(OTX())

    def get_request_info(self, data, group_name):
        request_infos = list()
        for api in self.api_list:
            request_infos = request_infos + api.get_task_info(data, group_name)

        return request_infos
