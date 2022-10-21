import os
import sys
import logging
import traceback
import argparse
from api.vt import VTApi
from file_manager import get_data_from_file
from log_manager import get_logger
from api.api_manager import ApiManager
from string_parser import check_str, is_file, get_group_name
from thread_pool_manager import ThreadPoolMgr


parser = argparse.ArgumentParser(
    description='상용 위협 인텔리전스 동향 조사 및 특징정보 수집 API 모듈')
parser.add_argument('input', help='파일명/IOC)')
parser.add_argument('-gn', '--groupName', type=str,
                    help="그룹명 지정 (기본값 : 파일명 -> 파일명(-ioc제외), IOC -> ETC")


class App:
    def __init__(self):
        self.logger = logging.getLogger()
        self.api_manager = ApiManager()
        self.thread_manager = ThreadPoolMgr()
        self.VT = VTApi()

    def __call__(self, str, group_name=None):
        try:
            data = dict()
            if is_file(str):
                data = get_data_from_file(str)
                if group_name == None:
                    group_name = get_group_name(str)
            else:
                data = check_str(str)
                group_name = "ETC"
            if data == None or len(data.keys()) == 0:
                self.logger.info("There is no data to request.")
                return
            self.VT.thread_run(data, group_name)
            result = self.api_manager.get_request_info(data, group_name)
            self.thread_manager(result)
        except Exception as e:
            self.logger.error(str(e))


if __name__ == "__main__":
    logger = logging.getLogger()
    try:
        logger = get_logger(logger)
        app = App()
        args = parser.parse_args()
        app(args.input, args.groupName)
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
