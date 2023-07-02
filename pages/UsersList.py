# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.01.02
# version ='1.0'
# ---------------------------------------------------------------------------
""" Users List page """
# ---------------------------------------------------------------------------from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class UsersListePage:
    def __init__(self, driver):
        self.driver = driver
        
    new_usr= (By.CSS_SELECTOR,"div[class='btn-new-user']")
    #table
    tbl_fname=(By.CSS_SELECTOR,"div.user-list.container div.table-container td:nth-child(1)")
    tbl_lname=(By.CSS_SELECTOR,"div.user-list.container div.table-container td:nth-child(2)")
    tbl_mobile=(By.CSS_SELECTOR,"div.user-list.container div.table-container td:nth-child(3)")
    tbl_clear_pas=(By.CSS_SELECTOR,"div.user-list.container div.table-container td:nth-child(4)")
    tbl_del_usr=(By.CSS_SELECTOR,"div.user-list.container div.table-container td:nth-child(5)")
    
    yes_no_del_usr=(By.CSS_SELECTOR,"div[class='yesno-modal-btns-wrapper']")
    yes_del_usr=(By.CSS_SELECTOR,"div[class='yesno-modal-btns-wrapper'] div[class='rectangle-button yesno-modal-button']:nth-child(1)")
    no_del_usr=(By.CSS_SELECTOR,"div[class='yesno-modal-btns-wrapper'] div[class='rectangle-button yesno-modal-button']:nth-child(2)")
    
    tbl_usr_row=(By.CSS_SELECTOR,"div.user-list.container div.table-container tbody tr")
    
    
    
    
    def getNewUser(self):
        return self.driver.find_element(*UsersListePage.new_usr).click()
    
    def DeleteNewUser(self):
        return self.driver.find_element(*UsersListePage.yes_del_usr).click()
    
    def CancelDelNewUser(self):
        return self.driver.find_element(*UsersListePage.no_del_usr).click()
    
    def getFirstNames(self):
        return self.driver.find_elements(*UsersListePage.tbl_fname)
    
    def getLastNames(self):
        return self.driver.find_elements(*UsersListePage.tbl_lname)
    
    
    def getMobile(self):
        return self.driver.find_elements(*UsersListePage.tbl_mobile)
    
    def getUserRows(self):
        return self.driver.find_elements(*UsersListePage.tbl_usr_row)
    
