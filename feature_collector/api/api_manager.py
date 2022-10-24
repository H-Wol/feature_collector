from api.urlhaus import URLHaus
from api.malware_bz import MalwareBazzar
from api.otx import OTX


class ApiManager():
    def __init__(self):
        """
        사용할 API 객체를 list로 추가
        """
        self.api_list = list()
        self.api_list.append(URLHaus())
        self.api_list.append(MalwareBazzar())
        self.api_list.append(OTX())

    def get_request_info(self, data, group_name):
        """
        IOC데이터를 각 API의 규격에 맞는 요청 데이터로 변환하여 반환
        """
        request_infos = list()
        for api in self.api_list:
            request_infos = request_infos + api.get_task_info(data, group_name)

        return request_infos
