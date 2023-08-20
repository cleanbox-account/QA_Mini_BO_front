from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class FailedSMS:

    def __init__(self, driver):
        self.driver = driver

    table = (By.CSS_SELECTOR,"table[class='sms-table']")
    
    download=(By.CSS_SELECTOR,"button[class='button export-btn']")

    def getSMSTable_exist(self):
        try :
            has_table=self.driver.find_element(*FailedSMS.table)
            return True
        except :
            return False


    def downloadReport(self):
        return self.driver.find_element(*FailedSMS.download).click()
