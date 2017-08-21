import os

import logging.handlers
from ..config.base_config import BaseConfig

dir = os.path.split(os.path.realpath(__file__))[0]

logsdir = os.path.join(dir,'..','logs')
if not os.path.exists(logsdir):
    os.mkdirs(logsdir)

logfile = os.path.join(logsdir,'log_file.txt')

fh = logging.handlers.RotatingFileHandler(logfile, mode='a', maxBytes=1024*30, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setLevel(BaseConfig.LOG_LEVEL)
fh.setFormatter(formatter)

def logger(name):
    log = logging.getLogger(name)
    log.setLevel(BaseConfig.LOG_LEVEL)
    log.addHandler(fh)
    return log
