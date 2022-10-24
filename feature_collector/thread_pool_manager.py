from concurrent.futures import ThreadPoolExecutor
import logging
from thread import Thread
from api.config.config import ConfigMgr
import traceback


class ThreadPoolMgr:

    def __init__(self):
        """_summary_
        Thread Pool의 Task와 설정 정보를 통해 executor 초기화
        """
        self.logger = logging.getLogger()
        self.task = Thread()
        self.config = ConfigMgr().get_instance()
        self.max_workers = int(
            self.config.get_config2("THREAD", "max_workers"))
        self.executor = ThreadPoolExecutor(max_workers=self.max_workers)

    def __call__(self, task_infos: list):
        """_summary_

        Args:
            task_infos (list): API 요청을 보낼 데이터
        """
        try:
            {self.executor.submit(self.task, task_info["type"], task_info["url"], task_info["header"],
                                  task_info["data"], task_info["save_dir"]): task_info for task_info in task_infos} # Thread Pool에 Task 정보를 보내 Thread 실행
        except Exception as e:
            self.logger.error(traceback.format_exc())
