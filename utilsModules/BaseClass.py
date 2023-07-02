# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2022.12.07
# version ='1.0'
# ---------------------------------------------------------------------------
"""  Base class, setup initialize with logger and elements verification functions """
# ---------------------------------------------------------------------------
import pytest
import logging
import inspect
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
loggers = {}  # new


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyElClassPresence(self, By_CLASS_text):
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By_CLASS_text)))
            return True
        except:
            return False

    def verifyElSelectorPresence(self, By_SELECTOR_text):
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By_SELECTOR_text)))
            return True
        except :
            return False
        
    def verifyCurrentURL(self,curr_url):
        try:
            wait=WebDriverWait(self.driver, 10)
            wait.until(EC.url_to_be(curr_url))
            return True
        except:
            return False   

    def getLogger(self, dir='test'):
        # global loggers
        now_date = datetime.now().strftime("%Y_%m_%d")
        filename = "C:\\TEST_ENV\\CleanBox_Project\\Mini_BackOffice\\Logs\\" + dir+"\\logfile_"+now_date+".log"
        fileHandler = logging.FileHandler(filename, encoding="UTF-8")  # utf-8 > possible to use Hebrew too
        formatter = logging.Formatter(
                "%(asctime)s : %(levelname)s : %(name)s:%(lineno)s : %(message)s")  # format of logs        
        loggerName = inspect.stack()[1][3]
        fileHandler.setFormatter(formatter)

        logger = logging.getLogger(loggerName)
        if logger.handlers:
            for handler in logger.handlers:
                logger.removeHandler(handler)
                
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger