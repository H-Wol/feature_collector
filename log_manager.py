import os
import gzip
import shutil
import logging
import logging.handlers

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class GZipRotator:
    def __call__(self, source, dest):
        os.rename(source, dest)
        f_in = open(dest, 'rb')
        save_file_name = self.namer(dest)
        f_out = gzip.open(save_file_name, 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        dir = self.isdir(dest)
        shutil.move(save_file_name, os.path.join(
            dir, os.path.basename(save_file_name)))
        os.remove(dest)

    def isdir(self, name):
        dir = os.path.dirname(name) + "/backup/" + \
            name.split(".")[-1].split("-")[0]+"-" + \
            name.split(".")[-1].split("-")[1]
        os.makedirs(dir, exist_ok=True)
        return dir

    def namer(self, name):
        return name.split(".")[0] + "." + name.split(".")[-1] + ".log.gz"


class LogHandler():
    def __init__(self, init_logger, name="logger", default_level="DEBUG"):
        self.log = init_logger
        self.log.propagate = True
        self.formatter = logging.Formatter(
            "[%(asctime)s.%(msecs)03d][%(levelname)s][%(filename)s:%(lineno)d] %(message)s", "%m/%d %H:%M:%S")
        self.levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL}
        self.log.setLevel(self.levels[default_level])
        os.makedirs("log", exist_ok=True)

    def stream_handler(self, level):
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(self.levels[level])
        streamHandler.setFormatter(self.formatter)
        self.log.addHandler(streamHandler)
        return self.log

    def timeRotate_handler(self, filename='./log/collector.log', when="D", level="DEBUG", atTime=None, interval=1):
        fileHandler = logging.handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,  # W0
            # backupCount=backupCount,
            interval=interval,
            atTime=atTime)
        fileHandler.rotator = GZipRotator()
        fileHandler.suffix = "%Y-%m-%d"
        fileHandler.setLevel(self.levels[level])
        fileHandler.setFormatter(self.formatter)
        self.log.addHandler(fileHandler)
        return self.log


def get_logger(init_logger):
    logger = LogHandler(init_logger)
    logger.stream_handler("INFO")
    logger = logger.timeRotate_handler(level="INFO")
    return logger
