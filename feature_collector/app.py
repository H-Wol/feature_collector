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
        self.api_manager = ApiManager()  # API 관리 모듈 선언 및 초기화
        self.thread_manager = ThreadPoolMgr()  # Thread Pool 선언 및 초기화
        self.VT = VTApi()  # 바이러스 토탈 요청 모듈 선언 및 초기화

    def __call__(self, str, group_name=None):
        try:
            data = dict()
            if is_file(str):  # 파일일 경우
                data = get_data_from_file(str) # 파일로부터 데이터 추출 {IOC_type : [data,data2], IOC_type2 : [data3,data4] } 형식
                if group_name == None: #입력받은 그룹명이 없을 경우
                    group_name = get_group_name(str) # 파일 명으로 그룹명 지정
                    
            else: # IOC인경우
                data = check_str(str) # 해당 IOC의 타입을 확인하여 {IOC_type : [str]} 형식으로 반환
                if group_name == None: #입력받은 그룹명이 없을 경우
                    group_name = "ETC" # ETC로 그룹명 지정
                    
            if data == None or len(data.keys()) == 0: #추출된 데이터가 없을경우 종료
                self.logger.info("There is no data to request.")
                return
            
            self.VT.thread_run(data, group_name) #바이러스 토탈 요청 모듈에 데이터와 그룹명을 전달하여 Thread 작업 진행 
            result = self.api_manager.get_request_info(data, group_name) #API 모듈을 통해 사용할 API들의 형식에 맞춰 데이터 생성
            """
            result = [{
                "type": "", GET/POST
                "url": "",  요청할 URL
                "header": dict(), 헤더
                "data": dict(), POST시 전달할 데이터
                "save_dir": "", 저장 경로
            }] 형식
            """
            # self.thread_manager(result) #Thread Pool에 위 데이터 전달하여 작업 진행
        except Exception as e:
            self.logger.error(str(e))


if __name__ == "__main__":
    logger = logging.getLogger()
    try:
        logger = get_logger(logger)
        app = App()
        args = parser.parse_args() # 입력받은 인자를 파싱
        app(args.input, args.groupName) #인자 전달하여 메인 코드 진행
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
