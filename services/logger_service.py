# python modules
import os
import logging
from datetime import datetime as dt
from logging.handlers import TimedRotatingFileHandler

"""
logger function
"""
logger = logging.getLogger("werkzeug")
base = "logs/"
monthDir = dt.now().strftime("%Y-%m/")
baseAndMonthDir = base + monthDir
if not os.path.exists(baseAndMonthDir):
    os.makedirs(baseAndMonthDir)
serviceName = "SS-EEB"
fileName = serviceName + ".log"
fullPath = baseAndMonthDir + fileName

handler = TimedRotatingFileHandler(fullPath, when="midnight", interval=1)
formatter = logging.Formatter(
    "%(levelname)s: [%(asctime)s] %(funcName)s(%(lineno)d) -- %(message)s",
    datefmt="%d/%b %H:%M:%S",
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
