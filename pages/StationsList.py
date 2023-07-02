# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.01.02
# version ='1.0'
# ---------------------------------------------------------------------------
""" Stations list page """
# ---------------------------------------------------------------------------from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class StationsPage:
    def __init__(self, driver):
        self.driver = driver