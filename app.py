import os
import sys
import json
import logging
import traceback
from api.vt import VTApi
from file_manager import get_data_from_file
from api.config.config import ConfigMgr
from log_manager import get_logger

class App:
    def __init__(self):
        self.logger = logging.getLogger()
        self.VT = VTApi()
    
    def __call__(self,*args):
        # self.logger.info(args)
        pass
    def test(self):
        data = get_data_from_file("IOCS/FamousSparrow-ioc_copy.csv")
        # print(data)
        self.VT.get_info(data,"FamousSparrow-ioc_copy")
        

if __name__ == "__main__":
    logger = logging.getLogger()
    try:
        logger = get_logger(logger)
        app = App()
        # app(sys.argv[1:])
        app.test()
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())